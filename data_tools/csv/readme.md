# CSV 工具集操作文档
Author: GPT4.0 & heike07
> 将包含表头的CSV文件批量导入至MYSQL

## 文件结构
```shell
|- csv_input_mysql.py 数据批量导入工具
|- cleaned_datas.py 数据批量文件清洗工具
|- differ_datas.py 数据批量比对工具
```

## 数据导入工具
csv_input_mysql.py
### 运行启动
启动脚本
```shell
直接执行：
python3 csv_input_mysql.py

或通过日志生成
nohup python3 csv_input_mysql.py > csv_input_mysql.log &

生成的文件名称 csv_input_mysql.log 可以根据情况修改，如果想保留全部日志可以将 > 替换为 >> 即可
```
查看日志
```shell
vim csv_input_mysql.log
```

### 调试DEBUG
字符串替换
```shell
table_name = os.path.splitext(filename)[0].replace('.', '-')
根据实际情况替换CSV文件中分隔符
```
Field_type
```shell
create_table_query += "`" + header.replace('"', '') + "` TEXT, "
根据实际情况调整字段类型
```

## ERR
常见错误
```shell
数据表格 `XXX` 创建失败: (1059, "Identifier name 'XXX' is too long")
表名过长，不能超过64字符，修改CSV文件名称

数据表格 `XXX2` 创建失败: (1118, 'Row size too large. The maximum row size for the used table type, not counting BLOBs, is 65535. This includes storage overhead, check the manual. You have to change some columns to TEXT or BLOBs')
设置为vchar(255)的字段长度不足与承载数据长度，尝试设置成TEXT或增大字段设置长度
```
字符集错误
```shell
  File "csv_input_mysql.py", line 40, in <module>
    headers = next(csv_reader)
  File "/usr/lib64/python3.6/codecs.py", line 321, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb4 in position 0: invalid start byte
初始文件中有中文，或者编码非utf8 ，此时需要修改代码中 uft8 替换为自己的编码 比如gbk、gb2312 等
```
数据源（windows&linux）
用于CSV生成的操作系统不同的换行符是不一样的。
```shell
导入过程中出现大类警告
'Warning', 1262, 'Row 64 was truncated; it contained more data than there were input columns'

修改 csv_input_mysql.py 中的
源数据为LINUX导出CSV换行修改为： LINES TERMINATED BY '\n'
源数据为WINDOES导出CSV换行修改为： LINES TERMINATED BY '\r\n'
```
依赖缺失错误
```shell
执行带字符编码检测的程序csv_input_data_chardet.py时提示
Traceback (most recent call last):
  File "csv_input_data_chardet.py", line 5, in <module>
    import chardet
ModuleNotFoundError: No module named 'chardet'
解决方法
pip3 install chardet
```

## 批量数据验证
源数据无法预估质量，会出现源数据换行等情况，此时可以使用批量清洗工具进行清洗，清洗后即可进行验证
### 如何批量验证？
```shell
通过数据导入程序进行导入程序后，对原始csv进行批量文件清洗
将原始文件 放入input文件夹{没有创建一下}

执行批量清洗程序
python3 cleaned_datas.py

执行后可以通过输出结果查询结果：

[root@ict181 db_cls]# python3 differ_datas_v3.py 
cleaned_xxl_job.xxl_job_1.csv: MySQL 行数 = 27, 清洗后行数 = 28, 数据校验 = 校验通过
cleaned_xxl_job.xxl_job_2.csv: MySQL 行数 = 621, 清洗后行数 = 622, 数据校验 = 校验通
cleaned_xxl_job.xxl_job_3.csv: MySQL 行数 = 1, 清洗后行数 = 2, 数据校验 = 校验通过
cleaned_xxl_job.xxl_job_4.csv: MySQL 行数 = 0, 清洗后行数 = 1, 数据校验 = 校验通过
cleaned_xxl_job.xxl_job_5.csv: MySQL 行数 = 73, 清洗后行数 = 74, 数据校验 = 校验通过
cleaned_xxl_job.xxl_job_6.csv: MySQL 行数 = 0, 清洗后行数 = 1, 数据校验 = 校验通过
cleaned_xxl_job.xxl_job_log.csv: MySQL 行数 = 74513, 清洗后行数 = 74514, 数据校验 = 校验通过
cleaned_xxl_job.xxl_job_info.csv: MySQL 行数 = 92, 清洗后行数 = 93, 数据校验 = 校验通过
所有文件的行数对比和数据校验工作已完成。

通过nohup进行后台执行参考前面执行方式
通过 | grep 进行日志筛选
```

祝您 工作顺利！