# XLSX 工具集操作文档
Author: GPT4.0 & heike07
> 将包含表头的XLS和XLSX文件批量导入至MYSQL

## 启动运行
```shell
# python3 xls_input_mysql.py
usage: xls_input_mysql_v8.py [-h] [--batch_size BATCH_SIZE]
                             [--field_type FIELD_TYPE]
                             directory
xls_input_mysql.py: error: the following arguments are required: directory

默认参数为 文件路径 批量插入行数 字段类型
根据自身需求进行运行

默认值：文件路径 必要参数 ；--batch_size 500 --field_type vchar(500)
```
## 执行示例
```shell
[root@ict181 tml]# python3 xls_input_mysql_v8.py ./xls_db/ --field_type "TEXT"
START | 2024-07-26 16:11:25
正在处理文件: ./xls_db/改-youfile.xlsx
检测到文件编码: utf-8
根据编码 `utf-8` 确定字符集: utf8mb4
数据表格 `改-youfile` 创建成功
数据插入成功，批次 1
END | 2024-07-26 16:11:26
总执行时间: 00:00:00

```
## ERR
依赖错误
```shell
正在处理文件: ./xls_db/youfile.xlsx
检测到文件编码: utf-8
根据编码 `utf-8` 确定字符集: utf8mb4
读取 Excel 文件失败: Missing optional dependency 'openpyxl'.  Use pip or conda to install openpyxl.
根据自身环境 选择安装
pip install pandas pymysql chardet xlrd

```
字段内容过长
```shell
数据插入失败: (1406, "Data too long for column '修补建议' at row 17")
使用TEXT参数进行插入
python3 xls_input_mysql_v8.py ./xls_db/ --field_type "TEXT"
```