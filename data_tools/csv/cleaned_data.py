# TITLE: cleaned_data ADD
# Author: GPT4 & heike07

# 脚本工具作用：清洗""字段中的换行情况以及空格，使其变为已（行）为单位的标准CSV

import csv

# 清洗前源数据
input_file = 'you_file.csv'
# 清洗后数据
output_file = 'cleaned_you_file.csv'

def clean_field(field):
    if isinstance(field, str):
        # 替换字段内的换行符（\n）和回车符（\r），保留引号
        field = field.replace('\n', ' ').replace('\r', ' ')
    return field

# 设置 csv 模块的最大字段大小
csv.field_size_limit(10000000)  # 增加字段大小限制为 10MB

with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
     open(output_file, mode='w', newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile, quotechar='"', quoting=csv.QUOTE_ALL)
    writer = csv.writer(outfile, quotechar='"', quoting=csv.QUOTE_ALL)

    for row in reader:
        cleaned_row = [clean_field(field) for field in row]
        writer.writerow(cleaned_row)

print(f'字段中的回车和换行符已清理，并保存到 {output_file}')
