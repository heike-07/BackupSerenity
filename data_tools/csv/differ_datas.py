# TITLE: differ_datas
# Author: GPT4 & heike07

# 脚本工具作用： 对清洗后的数据校验的批量对比工具
import os
import csv
import pymysql

# MySQL 配置
db_config = {
    'user': 'you is user',
    'password': 'you is password',
    'host': 'you is IP',
    'port': 3306,
    'database': 'you is database name',
    'local_infile': True,
}

# 清洗后数据目录
output_dir = 'output/'  # 替换为实际路径

# 连接到 MySQL 数据库
cnx = pymysql.connect(**db_config)
cursor = cnx.cursor()

def get_table_name(filename):
    # 从文件名中提取实际的表名，去除 'cleaned_' 前缀
    base_name = os.path.splitext(filename)[0]
    if base_name.startswith('cleaned_'):
        return base_name[len('cleaned_'):].replace('.', '-')
    return base_name.replace('.', '-')

def compare_csv_and_db(filename):
    table_name = get_table_name(filename)
    output_file = os.path.join(output_dir, filename)

    # 从 MySQL 表中获取记录数
    try:
        cursor.execute(f'SELECT COUNT(*) FROM `{table_name}`')
        mysql_count = cursor.fetchone()[0]
    except pymysql.err.ProgrammingError as e:
        print(f"Table `{table_name}` does not exist in database: {e}")
        mysql_count = None

    # 计算清洗后文件的行数
    with open(output_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        cleaned_line_count = sum(1 for _ in reader)

    # 判断数据校验是否正确
    header_line_count = 1  # 表头行数
    data_line_count = cleaned_line_count - header_line_count
    if mysql_count is not None:
        is_valid = data_line_count == mysql_count
        status = "校验通过" if is_valid else "校验失败"
        print(f'{filename}: MySQL 行数 = {mysql_count}, 清洗后行数 = {cleaned_line_count}, 数据校验 = {status}')
    else:
        print(f'{filename}: MySQL 行数 = N/A, 清洗后行数 = {cleaned_line_count}')

# 遍历输出目录中的所有CSV文件
for filename in os.listdir(output_dir):
    if filename.endswith('.csv'):
        compare_csv_and_db(filename)

# 关闭数据库连接
cursor.close()
cnx.close()

print("所有文件的行数对比和数据校验工作已完成。")
