# TITLE: xls_input_mysql
# Author: GPT4 & heike07

# 脚本工具作用：用于xls批量导入mysql
import os
import re
import pandas as pd
import pymysql
import time
from datetime import datetime
import argparse

# 确保 'openpyxl' 已安装并导入

def determine_charset(encoding):
    if encoding.lower() in ['utf-8', 'utf8']:
        return 'utf8mb4'
    elif encoding.lower() in ['gbk', 'gb2312']:
        return 'gbk'
    else:
        return 'utf8mb4'

def clean_column_name(column_name):
    return re.sub(r'[^\w]', '_', column_name)

def create_table(df, table_name, field_type, charset):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    columns = [clean_column_name(col) for col in df.columns]

    create_table_query = f"CREATE TABLE IF NOT EXISTS `{table_name}` ("
    for column in columns:
        create_table_query += f"`{column}` {field_type}, "
    create_table_query = create_table_query.rstrip(', ') + f") CHARSET={charset};"

    try:
        cursor.execute(create_table_query)
        connection.commit()
        print(f"数据表格 `{table_name}` 创建成功")
    except Exception as e:
        print(f"数据表格 `{table_name}` 创建失败: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()

def insert_data(df, table_name, batch_size):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    columns = [clean_column_name(col) for col in df.columns]

    df = df.where(pd.notnull(df), None)

    for i in range(0, len(df), batch_size):
        batch_df = df.iloc[i:i+batch_size]

        placeholders = ', '.join(['%s'] * len(columns))
        columns_str = ', '.join(columns)
        insert_query = f"INSERT INTO `{table_name}` ({columns_str}) VALUES ({placeholders})"

        try:
            cursor.executemany(insert_query, batch_df.values.tolist())
            connection.commit()
            print(f"数据插入成功，批次 {i // batch_size + 1}")
        except Exception as e:
            print(f"数据插入失败: {e}")
            connection.rollback()
    cursor.close()
    connection.close()

def process_excel_file(file_path, batch_size, field_type):
    print(f"正在处理文件: {file_path}")
    try:
        # 读取Excel文件
        df_dict = pd.read_excel(file_path, sheet_name=None, dtype=str, engine='openpyxl')  # 将所有数据读取为字符串
        encoding = 'utf-8'
        print(f"检测到文件编码: {encoding}")
        charset = determine_charset(encoding)
        print(f"根据编码 `{encoding}` 确定字符集: {charset}")

        for sheet_name, df in df_dict.items():
            table_name = os.path.splitext(os.path.basename(file_path))[0] + "_" + sheet_name
            table_name = clean_column_name(table_name)
            create_table(df, table_name, field_type, charset)
            insert_data(df, table_name, batch_size)
    except Exception as e:
        print(f"读取 Excel 文件失败: {e}")

def main():
    parser = argparse.ArgumentParser(description='将 Excel 数据导入 MySQL 数据库')
    parser.add_argument('directory', type=str, help='包含 Excel 文件的目录')
    parser.add_argument('--batch_size', type=int, default=500, help='数据批量插入大小')
    parser.add_argument('--field_type', type=str, default='VARCHAR(500)', help='数据库字段类型')
    args = parser.parse_args()

    print(f"START | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    start_time = time.time()

    for filename in os.listdir(args.directory):
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            file_path = os.path.join(args.directory, filename)
            process_excel_file(file_path, args.batch_size, args.field_type)

    end_time = time.time()
    duration = end_time - start_time
    print(f"END | {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"总执行时间: {datetime.utcfromtimestamp(duration).strftime('%H:%M:%S')}")

if __name__ == "__main__":
    db_config = {
        'user': 'root',
        'password': 'VU!YeGj^Eddm!drA',
        'host': '192.150.1.181',
        'port': 29306,
        'database': 'GW_DB_TEST',
        'local_infile': True,
    }

    main()

