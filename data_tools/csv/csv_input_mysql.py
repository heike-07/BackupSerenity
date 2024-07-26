import os
import csv
import pymysql
import re
import chardet
from datetime import datetime

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

# 记录脚本开始时间
start_time = datetime.now()
print(f"START | {start_time.strftime('%Y-%m-%d %H:%M:%S')}")

# 连接到数据库
connection = pymysql.connect(**db_config)
cursor = connection.cursor()

def detect_encoding(file_path):
    """使用 chardet 检测文件编码"""
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    return result['encoding']

def detect_line_ending(file_path):
    """检测文件的行结束符"""
    line_endings = {'\r\n': 0, '\n': 0, '\r': 0}
    with open(file_path, 'rb') as f:
        chunk = f.read(4096)  # 读取文件的前4096字节
        for line_ending in line_endings:
            line_endings[line_ending] = chunk.count(line_ending.encode())

    # 选择出现最多的行结束符
    detected_line_ending = max(line_endings, key=line_endings.get, default='\n')
    return detected_line_ending

def determine_charset(file_encoding):
    """根据文件编码确定字符集"""
    if file_encoding.lower() in ['utf-8', 'utf8']:
        return 'utf8mb4'
    elif file_encoding.lower() in ['gbk', 'gb2312']:
        return file_encoding.lower()
    else:
        return 'utf8mb4'

# 循环处理目录中的每个 CSV 文件
for filename in os.listdir(csv_dir):
    if filename.endswith('.csv'):
        file_path = os.path.join(csv_dir, filename)
        table_name = os.path.splitext(filename)[0].replace('.', '-')

        # 检测文件编码
        try:
            encoding = detect_encoding(file_path)
        except Exception as e:
            encoding = f"检测编码失败: {e}"

        # 检测文件的行结束符
        try:
            line_ending = detect_line_ending(file_path)
        except Exception as e:
            line_ending = f"检测行结束符失败: {e}"

        # 确定字符集
        charset = determine_charset(encoding)

        # 读取 CSV 文件的表头
        try:
            with open(file_path, 'r', encoding=encoding) as csv_file:
                csv_reader = csv.reader(csv_file)
                headers = next(csv_reader)
        except Exception as e:
            header_read_status = f"读取文件失败: {e}"
            print(f"导入文件名: {filename}|创建表名: {table_name}|文件字符编码: {encoding}|文件行结束符: {line_ending}|创建表结果: {header_read_status}|数据导入结果: 未开始")
            continue

        # 创建表（如果不存在）
        create_table_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ("
        for header in headers:
            # 去除列名中的双引号和其他不必要的特殊字符，包括不可见字符
            clean_header = re.sub(r'[^\w]', '', header.strip())
            create_table_query += f"`{clean_header}` TEXT, "
        create_table_query = create_table_query.rstrip(', ') + f") CHARSET={charset};"

        try:
            cursor.execute(create_table_query)
            connection.commit()
            table_creation_status = "数据表格创建成功"
        except Exception as create_error:
            table_creation_status = f"数据表格创建失败: {create_error}"
            connection.rollback()

        # 导入数据
        try:
            load_data_query = f"""
            LOAD DATA LOCAL INFILE '{file_path}'
            INTO TABLE `{table_name}`
            CHARACTER SET {charset}
            FIELDS TERMINATED BY ','
            OPTIONALLY ENCLOSED BY '"'
            ESCAPED BY '\\\\'
            LINES TERMINATED BY '{line_ending}'
            IGNORE 1 LINES;
            """
            cursor.execute(load_data_query)
            connection.commit()
            import_status = "数据导入成功"

            # 显示导入警告
            cursor.execute("SHOW WARNINGS")
            warnings = cursor.fetchall()
            if warnings:
                import_status += " 数据导入警告: " + " | ".join(str(warning) for warning in warnings)
        except Exception as load_error:
            import_status = f"数据导入失败: {load_error}"
            connection.rollback()

        # 确保行结束符显示正确
        line_ending_display = {'\r\n': 'Windows风格 (\\r\\n)', '\n': 'Unix风格 (\\n)', '\r': '旧Mac风格 (\\r)'}.get(line_ending, '未检测到')

        # 优化输出格式
        print(f"导入文件名: {filename} | 创建表名: {table_name} | 文件字符编码: {encoding} | 文件行结束符: {line_ending_display} | 创建表结果: {table_creation_status} | 数据导入结果: {import_status}")

# 关闭连接
cursor.close()
connection.close()

# 记录脚本结束时间
end_time = datetime.now()
print(f"END | {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"总执行时间: {end_time - start_time}")
