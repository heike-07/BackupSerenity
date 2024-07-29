# XLSX 工具集操作文档
Author: GPT4.0 & heike07
> 将包含表头的XLS和XLSX文件批量导入至MYSQL

## 文件结构
```shell
|- xls_input_mysql.py xls数据批量导入工具
|- xls_differ_mysql.py xls数据批量校验工具
```

## 启动运行
```shell
# python3 xls_input_mysql.py
usage: xls_input_mysql_v8.py [-h] [--batch_size BATCH_SIZE]
                             [--field_type FIELD_TYPE]
                             directory
xls_input_mysql.py: error: the following arguments are required: directory

默认参数为 必写 文件路径 -h 帮助 --batch_size 批量插入行数 默认值{500} --field_type 字段类型 默认值 {vchar(500)}
根据自身需求进行运行
```
## 执行示例
```shell
# python3 xls_input_mysql.py ./xls_db/ --field_type "TEXT"
START | 2024-07-26 16:11:25
正在处理文件: ./xls_db/改-youfile.xlsx
检测到文件编码: utf-8
根据编码 `utf-8` 确定字符集: utf8mb4
数据表格 `改-youfile` 创建成功
数据插入成功，批次 1
END | 2024-07-26 16:11:26
总执行时间: 00:00:00
```
## 数据校验
```shell
通过数据校验程序进行数据校验检查数据条数是否一致
# python3 xls_differ_mysql.py xls_db/
文件: youfile.xlsx | Sheet 页: sheet1 | XLS 数据条数: 327 | MySQL 表: youfile | MySQL 数据条数: 0
sheet1 - 数据条数不一致。
文件: 反youfile.xlsx | Sheet 页: sheet1 | XLS 数据条数: 327 | MySQL 表: 反_youfile | MySQL 数据条数: 0
sheet1 - 数据条数不一致。
文件: 改-youfile.xlsx | Sheet 页: sheet1 | XLS 数据条数: 327 | MySQL 表: 改-youfile | MySQL 数据条数: 327
sheet1 - 数据条数一致。
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
python3 xls_input_mysql.py ./xls_db/ --field_type "TEXT"
```
数据库链接信息不正确
```shell
# python3 xls_differ_mysql.py xls_db/
Traceback (most recent call last):
  File "/usr/local/lib/python3.6/site-packages/pymysql/connections.py", line 614, in connect
    (self.host, self.port), self.connect_timeout, **kwargs
  File "/usr/lib64/python3.6/socket.py", line 724, in create_connection
    raise err
  File "/usr/lib64/python3.6/socket.py", line 713, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "xls_differ_mysql.py", line 74, in <module>
    main()
  File "xls_differ_mysql.py", line 63, in main
    table_name
  File "xls_differ_mysql.py", line 24, in get_row_count_from_mysql
    database=database
  File "/usr/local/lib/python3.6/site-packages/pymysql/connections.py", line 353, in __init__
    self.connect()
  File "/usr/local/lib/python3.6/site-packages/pymysql/connections.py", line 664, in connect
    raise exc
pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '192.168.1.15' ([Errno 111] Connection refused)")
解决方法
检查数据库联系信息并修改xls_differ_mysql.py中的db_config函数参数 ↓

    # 数据库连接信息
    db_config = {
        'user': 'you is user',
        'password': 'you is password',
        'host': 'you is IP',
        'port': 3306,
        'database': 'you is database name',
    }
```