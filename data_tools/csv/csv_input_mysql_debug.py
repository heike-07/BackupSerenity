# TITLE: csv_input_mysql
# Author: GPT4 & heike07


# 依赖引入
import os
import csv
import pymysql
import re

# MySQL 配置
db_config = {
    'user': 'you is user',
    'password': 'you is password',
    'host': 'you is IP',
    'port': 3306,
    'database': 'you is database name',
    'local_infile': True,
}

# CSV 文件所在的目录
csv_dir = './db'

# 错误数据导入
# csv_dir = './db_err'

# 连接到数据库
print("START")
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

# 循环处理目录中的每个 CSV 文件
for filename in os.listdir(csv_dir):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_dir, filename)
        print(f"正在疯狂处理-请等待-啦啦啦 {file_path} ...")

        # 读取 CSV 文件的表头
        with open(file_path, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            headers = next(csv_reader)

        # 创建表（如果不存在） - 根据实际情况调整 replace
        table_name = os.path.splitext(filename)[0].replace('.', '-')
        create_table_query = "CREATE TABLE IF NOT EXISTS `{}` (".format(table_name)
        for header in headers:
            # 去除列名中的双引号和其他不必要的特殊字符，包括不可见字符
            clean_header = re.sub(r'[^\w]', '', header.strip())
            create_table_query += "`" + clean_header + "` TEXT, "
        create_table_query = create_table_query.rstrip(', ') + ") CHARSET=utf8mb4;"


        try:
            cursor.execute(create_table_query)
            connection.commit()
            print(f"数据表格 `{table_name}` 创建成功")
        except Exception as create_error:
            print(f"数据表格 `{table_name}` 创建失败: {create_error}")
            connection.rollback()
            continue

        # 导入数据
        try:
            load_data_query = f"""
            LOAD DATA LOCAL INFILE '{file_path}'
            INTO TABLE `{table_name}`
            CHARACTER SET utf8mb4
            FIELDS TERMINATED BY ','
            OPTIONALLY ENCLOSED BY '"'
            ESCAPED BY '\\\\'
            LINES TERMINATED BY '\n'
            IGNORE 1 LINES;
            """
            cursor.execute(load_data_query)
            connection.commit()
            print(f"{file_path} 数据导入成功")

            # 显示导入警告
            cursor.execute("SHOW WARNINGS")
            warnings = cursor.fetchall()
            if warnings:
                print(f"{file_path} 数据导入警告:")
                for warning in warnings:
                    print(warning)
        except Exception as load_error:
            print(f"{file_path} 数据导入失败: {load_error}")
            connection.rollback()

# 关闭连接
cursor.close()
connection.close()

print("END")
