# TITLE: IdAddInputCsvMysql
# Author: GPT4 & heike07

# 脚本工具作用： 新增ID字段以XLS路径下文件夹创建的表

import os
import pymysql
import re
import pandas as pd
import argparse

def clean_column_name(column_name):
    return re.sub(r'[^\w]', '_', column_name)

def add_id_column_if_not_exists(table_name):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # 检查表中是否已经存在 `id` 字段
    check_id_query = f"SHOW COLUMNS FROM `{table_name}` LIKE 'id';"
    cursor.execute(check_id_query)
    result = cursor.fetchone()

    if result:
        print(f"`{table_name}` 表中已存在 `id` 字段，无需添加")
    else:
        add_id_query = f"ALTER TABLE `{table_name}` ADD COLUMN `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;"
        try:
            cursor.execute(add_id_query)
            connection.commit()
            print(f"`id` 字段已成功添加到 `{table_name}` 表中")
        except Exception as e:
            print(f"添加 `id` 字段失败: {e}")
            connection.rollback()

    cursor.close()
    connection.close()

def process_tables_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.xls') or filename.endswith('.xlsx'):
            table_name_prefix = os.path.splitext(filename)[0]

            # 模拟读取每个 Excel 文件中的所有 Sheet 名，并构建对应的表名
            df_dict = pd.read_excel(os.path.join(directory, filename), sheet_name=None, dtype=str, engine='openpyxl')
            for sheet_name in df_dict.keys():
                table_name = f"{table_name_prefix}_{sheet_name}"
                table_name = clean_column_name(table_name)
                add_id_column_if_not_exists(table_name)

def main():
    parser = argparse.ArgumentParser(description='为 MySQL 中的表添加自增 ID 字段')
    parser.add_argument('directory', type=str, help='包含 Excel 文件的目录')
    args = parser.parse_args()

    process_tables_in_directory(args.directory)

if __name__ == "__main__":

    db_config = {
        'user': 'you is user',
        'password': 'you is password',
        'host': 'you is IP',
        'port': 3306,
        'database': 'you is database name',
        'local_infile': True,
    }

    main()

