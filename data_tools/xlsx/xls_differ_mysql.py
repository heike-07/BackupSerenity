# TITLE: xls_differ_mysql
# Author: GPT4 & heike07

# 脚本工具作用：用于xls批量比对mysql
import os
import re
import pandas as pd
import pymysql
import argparse

def clean_column_name(column_name):
    """清理列名，去除特殊字符"""
    return re.sub(r'[^\w]', '_', column_name)

def get_row_count_from_xls(file_path):
    """读取 XLS 文件并计算每个 sheet 页的数据条数"""
    df_dict = pd.read_excel(file_path, sheet_name=None, dtype=str, engine='openpyxl')
    sheet_counts = {sheet_name: len(df) for sheet_name, df in df_dict.items()}
    return sheet_counts

def get_row_count_from_mysql(host, port, user, password, database, table):
    """从 MySQL 数据库中获取表的记录数"""
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT COUNT(*) FROM `{table}`")
            result = cursor.fetchone()
            return result[0]
    finally:
        connection.close()

def main():
    parser = argparse.ArgumentParser(description='批量校验 Excel 数据与 MySQL 数据库中记录数是否一致')
    parser.add_argument('directory', type=str, help='包含 Excel 文件的目录')
    args = parser.parse_args()

    # 数据库连接信息
    db_config = {
        'user': 'you is user',
        'password': 'you is password',
        'host': 'you is IP',
        'port': 3306,
        'database': 'you is database name',
    }

    for filename in os.listdir(args.directory):
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            file_path = os.path.join(args.directory, filename)
            sheet_counts = get_row_count_from_xls(file_path)

            for sheet_name, xls_row_count in sheet_counts.items():
                table_name = os.path.splitext(filename)[0] + "_" + sheet_name
                table_name = clean_column_name(table_name)

                mysql_row_count = get_row_count_from_mysql(
                    db_config['host'],
                    db_config['port'],
                    db_config['user'],
                    db_config['password'],
                    db_config['database'],
                    table_name
                )

                print(f"文件: {filename} | Sheet 页: {sheet_name} | XLS 数据条数: {xls_row_count} | MySQL 表: {table_name} | MySQL 数据条数: {mysql_row_count}")

                if xls_row_count == mysql_row_count:
                    print(f"{sheet_name} - 数据条数一致。")
                else:
                    print(f"{sheet_name} - 数据条数不一致。")

if __name__ == "__main__":
    main()

