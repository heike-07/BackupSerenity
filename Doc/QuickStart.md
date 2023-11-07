# Quick start

## 1. Docker method（Docker 方式）

**Step 1：**
Create a temporary container and obtain the files inside the container
创建一个临时容器并获取容器内的文件

```
docker pull heike07/backupserenity
docker run -d --name backupserenity-temp backupserenity:2.0
cd /opt/
mkdir Backupserenity-EDR
docker cp backupserenity-temp:/Backupserenity/conf .
docker stop backupserenity-temp
docker rm backupserenity-temp
```

**Step 2：**
Mount and open container
安装并打开容器

```
cd Backupserenity-EDR
docker run -v /opt/Backupserenity-EDR/conf:/Backup-tools/conf -v /opt/Backupserenity-EDR/NFS_LINK_DISK:/NFS_LINK_DISK -itd --privileged=true --name backupserenity backupserenity:2.0 /usr/sbin/init
ll
```

**Step 3：**
Check if the service inside the container is normal
检查容器内的服务是否正常

```
docker exec -it backupserenity /bin/bash
[root@f1cb51c9196e /]# ps -aux
USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND
root 1 0.2 0.1 43124 3344 ? Ss 02:52 0:00 /usr/sbin/init
root 18 0.2 0.1 39060 3172 ? Ss 02:52 0:00 /usr/lib/systemd/systemd-journald
root 28 1.1 0.0 35056 1816 ? Ss 02:52 0:00 /usr/lib/systemd/systemd-udevd
dbus 44 0.0 0.1 58088 2112 ? Ss 02:53 0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork
root 47 0.0 0.0 24260 1556 ? Ss 02:53 0:00 /usr/lib/systemd/systemd-logind
root 49 0.0 0.0 24268 1572 ? Ss 02:53 0:00 /usr/sbin/crond -n
mysql 67 7.9 9.0 1124088 169428 ? Sl 02:53 0:02 /usr/sbin/mysqld --daemonize --pid-file=/var/run/mysqld/m
root 109 0.0 0.0 8088 860 tty1 Ss+ 02:53 0:00 /sbin/agetty --noclear tty1 linux
root 110 0.0 0.0 11828 1812 pts/1 Ss 02:53 0:00 /bin/bash
root 126 0.0 0.0 51732 1724 pts/1 R+ 02:53 0:00 ps -aux
[root@f1cb51c9196e /]#
```

**Step 4：**
Container usage
开始使用容器

```
[root@localhost Backupserenity-EDR]# docker exec backupserenity /Backup-tools/backupserenity
Usage: /Backup-tools/backupserenity <program_name>
```

For specific usage, please refer to the Quick Start section in the Github project
[https://github.com/heike-07/Backup-tools.git](https://github.com/heike-07/Backup-tools.git)

有关具体用法，请参阅Github项目中的“快速入门”部分
[https://github.com/heike-07/Backup-tools.git](https://github.com/heike-07/Backup-tools.git)

Wishing you a pleasant use! Heike07
祝你使用愉快！Heike07

### A. 程序使用

```powershell
# 程序使用方式
通过主函数调用模块实现程序调用，调用后可以在容器挂载卷查看结果，日志在容器内查看。
```

#### A.1 Backup_Mysqldump_All

```powershell
[root@localhost Backupserenity-EDR]# docker exec backupserenity /Backup-tools/backupserenity Backup_Mysqldump_All
```

需要在容器配置挂载卷conf 中配置相应的数据库参数，否则执行容器内默认的参数，通过执行容器指向函数命令可以执行对应程序，然后在容器挂载卷查看结果即可。

#### A.2 Backup_Mysqldump_One

```powershell
[root@localhost Backupserenity-EDR]# docker exec backupserenity /Backup-tools/backupserenity Backup_Mysqldump_One
```

需要在容器配置挂载卷conf 中配置相应的数据库参数，否则执行容器内默认的参数，通过执行容器指向函数命令可以执行对应程序，然后在容器挂载卷查看结果即可。

#### A.3 Backup_Mydumper_MultiThread_Database_All

```powershell
[root@localhost Backupserenity-EDR]# docker exec backupserenity /Backup-tools/backupserenity Backup_Mydumper_MultiThread_Database_All
```

前置条件：待处理数据库binlog开启

需要在容器配置挂载卷conf 中配置相应的数据库参数，否则执行容器内默认的参数，通过执行容器指向函数命令可以执行对应程序，然后在容器挂载卷查看结果即可。

#### A.4 Backup_Mydumper_MultiThread_Database_One

```powershell
[root@localhost Backupserenity-EDR]# docker exec backupserenity /Backup-tools/backupserenity Backup_Mydumper_MultiThread_Dtabase_One
```

前置条件：待处理数据库binlog开启

需要在容器配置挂载卷conf 中配置相应的数据库参数，否则执行容器内默认的参数，通过执行容器指向函数命令可以执行对应程序，然后在容器挂载卷查看结果即可。

#### A.5 Backup_XtraBackup_add

```powershell
[root@localhost Backupserenity-EDR]# docker exec backupserenity /Backup-tools/backupserenity Backup_XtraBackup_add
```

前置条件：待处理数据库binlog开启，且通过slave 在容器中执行相应的master节点，通过主从指向的方式接入binlog数据流后，conf配置容器内数据库参数（默认）即可进行数据库文件备份，首次备份为FULL全量备份，N+1次备份为Add增量备份

需要在容器配置挂载卷conf 中配置相应的数据库参数，否则执行容器内默认的参数，通过执行容器指向函数命令可以执行对应程序，然后在容器挂载卷查看结果即可。

## 2. Bin method（二进制方式）

Refer to the readme.md document (III., IV.) section
请参阅readme.md文档（III、IV）部分

## 3. Development mode（开发方式）

Refer to the readme.md document ( Ⅴ.) section
请参阅readme.md文档（Ⅴ.）部分