# csv_input_mysql
Author: GPT4.0 & heike07
> 将包含表头的CSV文件批量导入至MYSQL
## Run
启动脚本
```shell
nohup python3 csv_input_mysql.py > csv_input_mysql.log &
生成的文件名称 csv_input_mysql.log 可以根据情况修改，如果想保留全部日志可以将 > 替换为 >> 即可
```
## Log see
查看日志
```shell
vim csv_input_mysql.log
```
## Log err output -ERR
导出错误日志 [失败]
```shell
cat csv_input_mysql.log | grep '创建失败' > csv_input_mysql.log.ERR
```
## Log err see -ERR
查看错误日志 [失败]
```shell
vim csv_input_mysql.log.ERR
```
## Get csv files name -OK
获取全部CSV文件名称 [成功]
```shell
cat csv_input_mysql.log | grep '正在疯狂处理' | awk '{print $2}' > csv_files.list
```
## Get tables name -OK
获取全部表名称 [成功]
```shell
cat csv_input_mysql.log | grep '创建成功' | awk '{print $2}' > table_names.list
```

## Debug
调试

### Table_replace
字符串替换
```shell
table_name = os.path.splitext(filename)[0].replace('.', '-')
根据实际情况替换CSV文件中分隔符
```

### Field_type
```shell
create_table_query += "`" + header.replace('"', '') + "` TEXT, "
根据实际情况调整字段类型
```

### ERR
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

## 数据验证
源数据无法预估质量，会出现源数据换行等情况，此时可以使用清洗工具进行清洗，清洗后即可进行验证
### 如何验证？
```shell
通过数据导入程序进行导入程序后，对原始csv进行清洗
编辑 cleaned_data.py 文件修改

# 清洗前源数据
input_file = 'you_file.csv'
# 清洗后数据
output_file = 'cleaned_you_file.csv'

修改完成后进行执行
python3 cleaned_data.py

执行成功后通过wc命令进行行数获取
wc -l cleaned_you_file.csv

数据库通过
SELECT COUNT(1) FROM you_file

得出的数差值为1

数据验证成功！
```