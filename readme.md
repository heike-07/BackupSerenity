# BackupSerenity

## Ⅰ. 1. 程序说明

快速开始 QuickStart：[https://github.com/heike-07/Backup-tools/blob/main/Doc/QuickStart.md](https://github.com/heike-07/Backup-tools/blob/main/Doc/QuickStart.md)

![Doc/introduce.png](Doc/introduce.png)

**开源软件 BackupSerenity MySQL 数据库备份工具**

核心原理：通过 Go 封装的一套基于 MySQL 备份的思路工具……

通过 Go 封装的一套基于 MySQL 备份的思路工具，可以实现以下内容：

> 1. **Backup_Mysqldump_All**  
     该程序为 mysqldump 原生的全库数据库备份程序。

> 2. **Backup_Mysqldump_One**  
     该程序为 mysqldump 原生的单个数据库备份程序。

> 3. **Backup_Mydumper_MultiThread_Database_All**  
     该程序为多线程全量数据库备份程序。

> 4. **Backup_Mydumper_MultiThread_Database_One**  
     该程序为多线程单库全量数据库备份程序。

> 5. **Backup_XtraBackup_add**  
     该程序为 XtraBackup 增量备份程序，用于提供 MySQL 数据库的全量 + 增量备份程序。

> **适用于不同的 MySQL 备份场景**

**全量备份、增量备份、单库备份、多库备份、全库备份、binlog 备份、文件备份**

**应该差不多能覆盖所有的 MySQL 备份需求了吧。**

欢迎大家 Star ⭐ 谢谢！Thanks~

**作者**：heike07  
**开源中国收录软件链接**：[https://www.oschina.net/p/backupserenity](https://www.oschina.net/p/backupserenity)  
**Github**：[https://github.com/heike-07/Backup-tools](https://github.com/heike-07/Backup-tools)  
**Gitee(码云)**：[https://gitee.com/heike07code/Backup-tools](https://gitee.com/heike07code/Backup-tools)  
**B站视频讲解**：[https://space.bilibili.com/7152549/channel/collectiondetail?sid=1636805](https://space.bilibili.com/7152549/channel/collectiondetail?sid=1636805)

![image-20230817145834992](README.assets/image-20230817145834992.png)

## Ⅰ. 2. 开发流程说明

![Development](Doc/Development.png)

## Ⅱ. V1.1 开发进度

### 开发任务

1. _`OK.`_ - 思路建设
2. _`OK.`_ - 编写 readme-doc 文档
3. _`OK.`_ - 核心代码开发 Mysqldump 备份架构
4. _`OK.`_ - 核心代码开发 Mydumper 备份架构
5. _`OK.`_ - 核心代码开发 Xtrabackup 备份架构
6. _`OK.`_ - 使用 GO 封装
7. _`OK.`_ - 主程序和配置文件分离
8. _`OK.`_ - 合并主分支发布 Releases
9. _`OK.`_ - 文档细化

### 版本说明

- 核心底层代码开发
- 使用 GO 方式封装

## Ⅱ. V2.0 开发进度

### 开发任务

1. _`OK.`_ - 思路建设
2. _`OK.`_ - 编写 readme-doc 文档
3. _`OK.`_ - Docker images 镜像封装
4. _`OK.`_ - 研究 Docker run 启动方式
5. _`OK.`_ - 研究 Docker 变量参数调用、以及文件映射
6. _`OK.`_ - 封装镜像并发布至 Docker Hub，编写 overview
7. _`OK.`_ - Write Quick Start documentation
8. _`OK.`_ - 测试
9. _`OK.`_ - 打 Tag version 发布 Releases

### 版本说明

1. 新增判断当前环境是否为 Docker 的逻辑和函数
2. 新增 backupserenity 控制主程序
3. 去除容器内 crontab 定期任务逻辑
4. 修复 Docker exec 无法调度，提示 exit 1 的问题
5. 解决 systemd 无法在容器中执行的问题
6. 实现 Docker 容器化封装，运行

## Ⅱ. V2.1 开发进度

### 开发任务

1. _`OK.`_ - 思路建设
2. _`ING.`_ - 编写 readme-doc 文档
3. _`OK.`_ - 实现 Docker Compose 运行
4. _`DEL.`_ - 接入 Minio Docker Compose 逻辑
5. _`DEL.`_ - 修复存储桶 bucket 不能为 IP 地址命名问题
6. _`DEL.`_ - 增加存储参数设置提示，不能以 IP 命名
7. _`OK.`_ - 删除存储桶 bucket 相关架构设计
8. _`OK.`_ - 研究 nginx 实现文件下载和查看，并设置加密（本地）
9. _`OK.`_ - 研究 nginx 实现文件下载和查看，并设置加密（Dockerfile），并设置为可选项
10. _`OK.`_ - 将 ngx-fancyindex 与 basic 加密封装为 image 并构建镜像
11. _`OK.`_ - 生成为 Docker Compose，并以可选组件运行
12. _`OK.`_ - 打 Tag version 发布 Releases

### 版本说明

1. 新增 Docker Compose 构建程序
2. 更新 backupserenity 镜像 image 到 2.0
3. 新增 backupserenity-nginx 镜像 image 到 2.1
4. 调试冗余文档编辑
5. 新增备份结果通过 nginx 加密查看和下载功能

---

## Ⅲ. V2.2 开发进度

### 开发任务

1. _`OK.`_ - 解决批量导入数据问题

### 版本说明

跳转更新内容：[https://github.com/heike-07/BackupSerenity/tree/main/data_tools](https://github.com/heike-07/BackupSerenity/tree/main/data_tools)

1. wip - 🕔 新增：CSV 文件批量导入工具集
2. wip - 🕔 新增：XLSX 文件批量导入工具集
