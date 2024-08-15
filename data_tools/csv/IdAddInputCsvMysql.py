# TITLE: IdAddInputCsvMysql
# Author: GPT4 & heike07

# 脚本工具作用： 新增ID字段以csv路径下文件夹创建的表

import os
import pymysql
import sys

# MySQL 配置
db_config = {
    'user': 'you is user',
    'password': 'you is password',
    'host': 'you is IP',
    'port': 3306,
    'database': 'you is database name',
    'local_infile': True,
}

def add_id_column_if_not_exists(table_name):
    """检查并为表添加 id 字段"""
    check_id_query = f"SHOW COLUMNS FROM `{table_name}` LIKE 'id';"
    cursor.execute(check_id_query)
    result = cursor.fetchone()

    if not result:
        add_id_query = f"ALTER TABLE `{table_name}` ADD COLUMN `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;"
        try:
            cursor.execute(add_id_query)
            connection.commit()
            print(f"`id` 字段已成功添加到 `{table_name}` 表中")
        except Exception as e:
            print(f"添加 `id` 字段失败: {e}")
            connection.rollback()
    else:
        print(f"`{table_name}` 表中已存在 `id` 字段，无需添加")

def process_csv_files_in_directory(directory):
    """处理指定目录中的 CSV 文件"""
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            # 获取表名
            table_name = os.path.splitext(filename)[0].replace('.', '-')

            # 调用函数为表添加 id 字段
            add_id_column_if_not_exists(table_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请提供 CSV 文件夹的路径作为参数")
        sys.exit(1)

    # 从命令行参数获取目录路径
    csv_dir = sys.argv[1]

    # 连接到数据库
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # 处理目录中的 CSV 文件
    process_csv_files_in_directory(csv_dir)

    # 关闭连接
    cursor.close()
    connection.close()

    print("所有表的处理已完成。")

