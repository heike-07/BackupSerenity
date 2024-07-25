# TITLE: csv_input_mysql
# Author: GPT4 & heike07

# 脚本工具作用：批量清洗""字段中的换行情况以及空格，使其变为已（行）为单位的标准CSV

import os
import csv

# 原始数据目录和清洗后数据目录
input_dir = 'input/'  # 替换为实际路径
output_dir = 'output/'  # 替换为实际路径

def clean_field(field):
    if isinstance(field, str):
        # 替换字段内的换行符（\n）和回车符（\r），保留引号
        field = field.replace('\n', ' ').replace('\r', ' ')
    return field

# 设置 csv 模块的最大字段大小
csv.field_size_limit(10000000)  # 增加字段大小限制为 10MB

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

print("清洗规则：替换字段内的换行符（\n）和回车符（\r），保留引号，使清洗结果 [wc -l] 行数 = 数据条数")
# 遍历输入目录中的所有CSV文件
for filename in os.listdir(input_dir):
    if filename.endswith('.csv'):
        input_file = os.path.join(input_dir, filename)
        output_file = os.path.join(output_dir, f'cleaned_{filename}')

        # 计算原始文件的行数
        with open(input_file, 'r', encoding='utf-8') as infile:
            original_line_count = sum(1 for _ in infile)

        # 进行清洗并计算清洗后文件的行数
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
             open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

            reader = csv.reader(infile, quotechar='"', quoting=csv.QUOTE_ALL)
            writer = csv.writer(outfile, quotechar='"', quoting=csv.QUOTE_ALL)

            cleaned_line_count = 0
            for row in reader:
                cleaned_row = [clean_field(field) for field in row]
                writer.writerow(cleaned_row)
                cleaned_line_count += 1

        print(f'{filename}: 原始数据行数 = {original_line_count}, 清洗后数据行数 = {cleaned_line_count}')

print("系统提示：所有文件的清洗工作已完成。")
