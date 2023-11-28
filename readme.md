# BackupSerenity

## Ⅰ. 1.程序说明

快速开始QuickStart：[https://github.com/heike-07/Backup-tools/blob/main/Doc/QuickStart.md](https://github.com/heike-07/Backup-tools/blob/main/Doc/QuickStart.md)

![Doc/introduce.png](Doc/introduce.png)

**开源软件 BackupSerenity MySQL 数据库备份工具** 

核心原理：通过 go 封装的一套基于 MySQL 备份的思路工具……

通过 go 封装的一套基于 MySQL 备份的思路工具，可以实现以下内容：

> 1.Backup_Mysqldump_All

该程序为 mysqldump 原生的全库数据库备份程序。

> 2.Backup_Mysqldump_One

该程序为 mysqldump 原生的单个数据库备份程序。

> 3.Backup_Mydumper_MultiThread_Database_All

该程序为多线程全量数据库备份程序

> 4.Backup_Mydumper_MultiThread_Database_One

该程序为多线程单库全量数据库备份程序

> 5.Backup_XtraBackup_add

该程序为 XtraBackup 增量备份程序，用于提供 MySQL 数据库的全量 + 增量备份程序

>>> **适用于不同的 MYSQL 备份场景**

**全量备份、增量备份、单库备份、多库备份、全库备份、binlog 备份、文件备份**

**应该差不多能覆盖所有的 MySQL 备份需求了吧。**

欢迎大家 star ⭐ 谢谢！ thanks~

作者： heike07 

开源中国收录软件链接：https://www.oschina.net/p/backupserenity 

Github：https://github.com/heike-07/Backup-tools 

Gitee(码云)：https://gitee.com/heike07code/Backup-tools 

B站视频讲解：https://space.bilibili.com/7152549/channel/collectiondetail?sid=1636805

![image-20230817145834992](README.assets/image-20230817145834992.png)

## Ⅰ. 2. 开发流程说明
![Development](Doc/Development.png)

## Ⅱ V1.1 开发进度

### 开发任务
1. _`OK.`_ - 思路建设
2. _`OK.`_ - 编写readme-doc文档
3. _`OK.`_ - 核心代码开发Mysqldump备份架构
4. _`OK.`_ - 核心代码开发Mydumper备份架构
5. _`OK.`_ - 核心代码开发Xtrabackup备份架构
6. _`OK.`_ - 使用GO封装
7. _`OK.`_ - 主程序和配置文件分离
8. _`OK.`_ - 合并主分支发布Releases
9. _`OK.`_ - 文档细化

### 版本说明

1.核心底层代码开发  
2.使用GO方式封装

## Ⅱ V2.0 开发进度

### 开发任务
1. _`OK.`_ - 思路建设
2. _`OK.`_ - 编写readme-doc文档
3. _`OK.`_ - docker images 镜像封装
4. _`OK.`_ - 研究dokcer run 启动方式
5. _`OK.`_ - 研究dokcer 变量参数调用、以及文件映射
6. _`OK.`_ - 封装镜像 发布至docker hub 并编写overview
7. _`OK.`_ - Write Quick Start documentation
8. _`OK.`_ - 测试
9. _`OK.`_ - 打tag version 发布 releases

### 版本说明

1. 新增判断当前环境是否为docker的逻辑和函数
2. 新增backupserenity 控制主程序
3. 去除容器内crontab 定期任务逻辑
4. 修复docker exec 无法调度 提示exit 1的问题
5. 解决systemd 无法在容器中执行
6. 实现docker容器化封装，运行

## Ⅱ V2.1 开发进度

### 开发任务

1. _`OK.`_ - 思路建设
2. _`ING.`_ - 编写readme-doc文档
3. _`OK.`_ - 实现docker-compose运行
4. _`DEL.`_ - 接入minio docker-compose逻辑
5. _`DEL.`_ - 修复存储桶bucket不能为IP地址命名问题
6. _`DEL.`_ - 增加存储参数设置提示不能以IP命名
7. _`OK.`_ - 删除存储桶bucket相关架构设计
8. _`OK.`_ - 研究下nginx实现文件下载和查看并设置加密（本地）
9. _`OK.`_ - 研究下nginx实现文件下载和查看并设置加密（Dockerfile）并设置为可选项
10. _`OK.`_ - 将ngx-fancyindex与basic加密封装为image并构建镜像
11. _`OK.`_ - 生成为docker-compose，并以可选组件运行
12. _`OK.`_ - 打tag version 发布 releases


### 版本说明

1. 新增docker-comoose构建程序
2. 更新backupserenity 镜像image 到2.0
3. 新增backupserenity-nginx 镜像image 到2.1
4. 调试冗余文档编辑
5. 新增备份结果通过nginx加密查看下载
---

