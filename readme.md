# BackupSerenity

![image-20230817143005605](README.assets/image-20230817143005605.png)


## Ⅰ. 程序说明
**开源软件 BackupSerenity MySQL 数据库备份工具** 

核心原理：通过 go 封装的一套基于 MySQL 备份的思路工具……

作者： heike07 

开源中国收录软件链接：https://www.oschina.net/p/backupserenity 

Github：https://github.com/heike-07/Backup-tools 

Gitee(码云)：https://gitee.com/heike07code/Backup-tools 

B站视频讲解：https://space.bilibili.com/7152549/channel/collectiondetail?sid=1636805

![image-20230817145834992](README.assets/image-20230817145834992.png)

欢迎大家star ⭐ 谢谢！ thanks~



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
1. _`ING.`_ - 思路建设
2. _`ING.`_ - 编写readme-doc文档
3. _`ING.`_ - docker images 镜像封装
4. _`ING.`_ - 研究dokcer run 启动方式
5. _`ING.`_ - 研究dokcer 变量参数调用、以及文件映射
6. _`ING.`_ - 研究dockercompose 启动方式
7. _`ING.`_ - 封装镜像 发布至docker hub
8. _`ING.`_ - Write quick-use documentation
9. _`ING.`_ - 测试
10. _`ING.`_ - 打tag version 发布 releases

### 版本说明

努力开发中……

---


## Ⅲ. 底层环境构建
### 1. 操作系统适用
适用于Centos7、Redhat7 操作系统，支持X86_64 架构，可以运行GO,shell的操作系统，其他系统适配中……
### 2. mysql或mariadb数据库

--（因为本机为实验环境没有MySQL则需要安装）

####  2/0 查询相关服务是否安装

```shell
[root@localhost mysql]# rpm -qa | grep mariadb
[root@localhost mysql]# rpm -qa | grep mysql
```

#### 2/1 下载MysqlRPM包
```shell
## 1:下载MysqlRPM包
[root@localhost soft]# wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.42-1.el7.x86_64.rpm-bundle.tar
[root@localhost soft]# mkdir ./mysql_5.7.42
[root@localhost soft]# tar -xvf mysql-5.7.42-1.el7.x86_64.rpm-bundle.tar -C ./mysql_5.7.42/
mysql-community-client-5.7.42-1.el7.x86_64.rpm
mysql-community-common-5.7.42-1.el7.x86_64.rpm
mysql-community-devel-5.7.42-1.el7.x86_64.rpm
mysql-community-embedded-5.7.42-1.el7.x86_64.rpm
mysql-community-embedded-compat-5.7.42-1.el7.x86_64.rpm
mysql-community-embedded-devel-5.7.42-1.el7.x86_64.rpm
mysql-community-libs-5.7.42-1.el7.x86_64.rpm
mysql-community-libs-compat-5.7.42-1.el7.x86_64.rpm
mysql-community-server-5.7.42-1.el7.x86_64.rpm
mysql-community-test-5.7.42-1.el7.x86_64.rpm
[root@localhost soft]# cd ./mysql_5.7.42/
```
#### 2/2 检查mariadb依赖

```shell
## 2:检查mariadb依赖 
--（默认安装的系统都有）
[root@localhost mysql_5.7.42]# rpm -qa | grep mariadb
mariadb-libs-5.5.68-1.el7.x86_64
[root@localhost mysql_5.7.42]# rpm -e --nodeps mariadb-libs-5.5.68-1.el7.x86_64
[root@localhost mysql_5.7.42]# rpm -qa | grep mariadb
[root@localhost mysql_5.7.42]# 
```
#### 2/3 安装MySQL
```shell
## 3:安装MySQL
[root@localhost mysql_5.7.42]# rpm -ivh mysql-community-common-5.7.42-1.el7.x86_64.rpm 
warning: mysql-community-common-5.7.42-1.el7.x86_64.rpm: Header V4 RSA/SHA256 Signature, key ID 3a79bd29: NOKEY
Preparing...                          ################################# [100%]
Updating / installing...
   1:mysql-community-common-5.7.42-1.e################################# [100%]
[root@localhost mysql_5.7.42]# rpm -ivh mysql-community-libs-5.7.42-1.el7.x86_64.rpm 
warning: mysql-community-libs-5.7.42-1.el7.x86_64.rpm: Header V4 RSA/SHA256 Signature, key ID 3a79bd29: NOKEY
Preparing...                          ################################# [100%]
Updating / installing...
   1:mysql-community-libs-5.7.42-1.el7################################# [100%]
[root@localhost mysql_5.7.42]# rpm -ivh mysql-community-client-5.7.42-1.el7.x86_64.rpm 
warning: mysql-community-client-5.7.42-1.el7.x86_64.rpm: Header V4 RSA/SHA256 Signature, key ID 3a79bd29: NOKEY
Preparing...                          ################################# [100%]
Updating / installing...
   1:mysql-community-client-5.7.42-1.e################################# [100%]
[root@localhost mysql_5.7.42]# rpm -ivh mysql-community-server-5.7.42-1.el7.x86_64.rpm 
warning: mysql-community-server-5.7.42-1.el7.x86_64.rpm: Header V4 RSA/SHA256 Signature, key ID 3a79bd29: NOKEY
Preparing...                          ################################# [100%]
Updating / installing...
   1:mysql-community-server-5.7.42-1.e################################# [100%]
[root@localhost mysql_5.7.42]# rpm -ivh mysql-community-devel-5.7.42-1.el7.x86_64.rpm 
warning: mysql-community-devel-5.7.42-1.el7.x86_64.rpm: Header V4 RSA/SHA256 Signature, key ID 3a79bd29: NOKEY
Preparing...                          ################################# [100%]
Updating / installing...
   1:mysql-community-devel-5.7.42-1.el################################# [100%]
[root@localhost mysql_5.7.42]# rpm -qa | grep mysql
mysql-community-server-5.7.42-1.el7.x86_64
mysql-community-common-5.7.42-1.el7.x86_64
mysql-community-devel-5.7.42-1.el7.x86_64
mysql-community-libs-5.7.42-1.el7.x86_64
mysql-community-client-5.7.42-1.el7.x86_64
[root@localhost mysql_5.7.42]# 
```
#### 2/4 自定义data存储路径
```shell
## 4:自定义data存储路径
[root@localhost mysql_5.7.42]# mkdir -p /data/mysql
[root@localhost mysql_5.7.42]# chown -R mysql:mysql /data/mysql
[root@localhost mysql_5.7.42]# vim /etc/my.cnf
[root@localhost mysql_5.7.42]# cat /etc/my.cnf
# For advice on how to change settings please see
# http://dev.mysql.com/doc/refman/5.7/en/server-configuration-defaults.html

[mysqld]
#
# Remove leading # and set to the amount of RAM for the most important data
# cache in MySQL. Start at 70% of total RAM for dedicated server, else 10%.
# innodb_buffer_pool_size = 128M
#
# Remove leading # to turn on a very important data integrity option: logging
# changes to the binary log between backups.
# log_bin
#
# Remove leading # to set options mainly useful for reporting servers.
# The server defaults are faster for transactions and fast SELECTs.
# Adjust sizes as needed, experiment to find the optimal values.
# join_buffer_size = 128M
# sort_buffer_size = 2M
# read_rnd_buffer_size = 2M
datadir=/data/mysql
socket=/data/mysql/mysql.sock

# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0

log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid

lower_case_table_names=1
max_connections=500
init_connect='SET NAMES utf8'

[client]
socket=/data/mysql/mysql.sock

[mysql]
socket=/data/mysql/mysql.sock
[root@localhost mysql_5.7.42]# 
```
#### 2/5 开启MySQL服务并设置密码以及权限
```shell
## 5:开启MySQL服务并设置密码以及权限
[root@localhost mysql_5.7.42]# systemctl start mysqld
[root@localhost mysql_5.7.42]# grep 'temporary password' /var/log/mysqld.log
2023-07-06T06:59:55.413788Z 1 [Note] A temporary password is generated for root@localhost: #Sb)2-w6yhd,
[root@localhost mysql_5.7.42]# mysql -uroot -p
Enter password: 
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: YES)
[root@localhost mysql_5.7.42]# mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.42

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'A16&b36@@';
Query OK, 0 rows affected (0.01 sec)

mysql> GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'A16&b36@@' WITH GRANT OPTION;
Query OK, 0 rows affected, 1 warning (0.00 sec)

mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)

mysql> exit
Bye
[root@localhost mysql_5.7.42]#
```
#### 2/6 开启binlog
```shell
## 6:开启binlog
[root@localhost mysql_5.7.42]# head -n 35 /etc/my.cnf
# For advice on how to change settings please see
# http://dev.mysql.com/doc/refman/5.7/en/server-configuration-defaults.html

[mysqld]
#
# Remove leading # and set to the amount of RAM for the most important data
# cache in MySQL. Start at 70% of total RAM for dedicated server, else 10%.
# innodb_buffer_pool_size = 128M
#
# Remove leading # to turn on a very important data integrity option: logging
# changes to the binary log between backups.
# log_bin
#
# Remove leading # to set options mainly useful for reporting servers.
# The server defaults are faster for transactions and fast SELECTs.
# Adjust sizes as needed, experiment to find the optimal values.
# join_buffer_size = 128M
# sort_buffer_size = 2M
# read_rnd_buffer_size = 2M
datadir=/data/mysql
socket=/data/mysql/mysql.sock

# Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0

log-error=/var/log/mysqld.log
pid-file=/var/run/mysqld/mysqld.pid

lower_case_table_names=1
max_connections=500
init_connect='SET NAMES utf8'

log-bin=mysql-bin
server-id=1

[root@localhost mysql_5.7.42]# 
[root@localhost mysql_5.7.42]# systemctl restart mysqld
[root@localhost mysql_5.7.42]# cd /data/
[root@localhost data]# ll
total 4
drwxr-xr-x 5 mysql mysql 4096 Jul  6 15:08 mysql
[root@localhost data]# cd mysql/
[root@localhost mysql]# ll
total 122960
-rw-r----- 1 mysql mysql       56 Jul  6 14:59 auto.cnf
-rw------- 1 mysql mysql     1676 Jul  6 14:59 ca-key.pem
-rw-r--r-- 1 mysql mysql     1112 Jul  6 14:59 ca.pem
-rw-r--r-- 1 mysql mysql     1112 Jul  6 14:59 client-cert.pem
-rw------- 1 mysql mysql     1676 Jul  6 14:59 client-key.pem
-rw-r----- 1 mysql mysql      350 Jul  6 15:08 ib_buffer_pool
-rw-r----- 1 mysql mysql 12582912 Jul  6 15:08 ibdata1
-rw-r----- 1 mysql mysql 50331648 Jul  6 15:08 ib_logfile0
-rw-r----- 1 mysql mysql 50331648 Jul  6 14:59 ib_logfile1
-rw-r----- 1 mysql mysql 12582912 Jul  6 15:08 ibtmp1
drwxr-x--- 2 mysql mysql     4096 Jul  6 14:59 mysql
-rw-r----- 1 mysql mysql      154 Jul  6 15:08 mysql-bin.000001
-rw-r----- 1 mysql mysql       19 Jul  6 15:08 mysql-bin.index
srwxrwxrwx 1 mysql mysql        0 Jul  6 15:08 mysql.sock
-rw------- 1 mysql mysql        5 Jul  6 15:08 mysql.sock.lock
drwxr-x--- 2 mysql mysql     8192 Jul  6 14:59 performance_schema
-rw------- 1 mysql mysql     1680 Jul  6 14:59 private_key.pem
-rw-r--r-- 1 mysql mysql      452 Jul  6 14:59 public_key.pem
-rw-r--r-- 1 mysql mysql     1112 Jul  6 14:59 server-cert.pem
-rw------- 1 mysql mysql     1680 Jul  6 14:59 server-key.pem
drwxr-x--- 2 mysql mysql     8192 Jul  6 14:59 sys
[root@localhost mysql]# 
[root@localhost mysql]# firewall-cmd --permanent --zone=public --add-port=3306/tcp
success
[root@localhost mysql]# firewall-cmd --reload
success
[root@localhost mysql]# ss -lnpt | grep 3306
LISTEN     0      128       [::]:3306                  [::]:*                   users:(("mysqld",pid=3399,fd=30))
[root@localhost mysql]# firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: ens33
  sources: 
  services: dhcpv6-client mountd nfs rpc-bind ssh
  ports: 3306/tcp
  protocols: 
  masquerade: no
  forward-ports: 
  source-ports: 
  icmp-blocks: 
  rich rules: 
        
[root@localhost mysql]# 
```
### 3. NFS环境安装

#### 3/0 查询相关服务

```shell
# 查询相关服务
[root@localhost ~]# systemctl status nfs*
如果没有则需要安装
```
#### 3/1 SELiunx 关闭

```shell
## 1:SELiunx 关闭
[root@localhost ~]# getsebool 
getsebool:  SELinux is disabled
```
#### 3/2 安装NFS

```shell
## 2:安装NFS
[root@localhost ~]# yum install nfs-utils
```
#### 3/3 查看rpcbind监听以及服务

```shell
## 3:查看rpcbind监听以及服务
[root@localhost ~]# ss -tnulp | grep 111
udp    UNCONN     0      0         *:111                   *:*                   users:(("rpcbind",pid=720,fd=6))
udp    UNCONN     0      0      [::]:111                [::]:*                   users:(("rpcbind",pid=720,fd=9))
tcp    LISTEN     0      128       *:111                   *:*                   users:(("rpcbind",pid=720,fd=8))
tcp    LISTEN     0      128    [::]:111                [::]:*                   users:(("rpcbind",pid=720,fd=11))
[root@localhost ~]# systemctl status rpcbind
● rpcbind.service - RPC bind service
   Loaded: loaded (/usr/lib/systemd/system/rpcbind.service; enabled; vendor preset: enabled)
   Active: active (running) since Thu 2023-07-06 13:26:29 CST; 34min ago
 Main PID: 720 (rpcbind)
   CGroup: /system.slice/rpcbind.service
           └─720 /sbin/rpcbind -w

Jul 06 13:26:28 localhost.localdomain systemd[1]: Starting RPC bind service...
Jul 06 13:26:29 localhost.localdomain systemd[1]: Started RPC bind service.
[root@localhost ~]# 
```
#### 3/4 防火墙开通端口

```shell
## 4:防火墙开通端口
[root@localhost ~]# firewall-cmd --permanent --add-service=rpc-bind
FirewallD is not running
[root@localhost ~]# systemctl status firewalld
● firewalld.service - firewalld - dynamic firewall daemon
   Loaded: loaded (/usr/lib/systemd/system/firewalld.service; disabled; vendor preset: enabled)
   Active: inactive (dead)
     Docs: man:firewalld(1)
[root@localhost ~]# systemctl start firewalld
[root@localhost ~]# systemctl enable firewalld
Created symlink from /etc/systemd/system/dbus-org.fedoraproject.FirewallD1.service to /usr/lib/systemd/system/firewalld.service.
Created symlink from /etc/systemd/system/multi-user.target.wants/firewalld.service to /usr/lib/systemd/system/firewalld.service.
[root@localhost ~]# firewall-cmd --permanent --add-service=rpc-bind
success
[root@localhost ~]# firewall-cmd --permanent --add-service=nfs
success
[root@localhost ~]# firewall-cmd --permanent --add-service=mountd
success
[root@localhost ~]# firewall-cmd --reload
success
[root@localhost ~]# firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: ens33
  sources: 
  services: dhcpv6-client mountd nfs rpc-bind ssh
  ports: 
  protocols: 
  masquerade: no
  forward-ports: 
  source-ports: 
  icmp-blocks: 
  rich rules: 
        
[root@localhost ~]# 
```
#### 3/5 创建路径编写可读可写权限

```shell
## 5:创建路径编写可读可写权限
[root@localhost ~]# mkdir /Nfs_Disk
[root@localhost ~]# echo "/Nfs_Disk 127.0.0.1/24(rw,async)" >> /etc/exports
[root@localhost ~]# cat /etc/exports
/Nfs_Disk 127.0.0.1/24(rw,async)
[root@localhost ~]# 
```
#### 3/6 添加NFS硬盘

```shell
## 6:添加NFS硬盘
--（可以做RAID硬件组保证数据高可用）
[root@localhost ~]# blkid
/dev/sda1: UUID="3ae6a4b1-0140-4d7d-b8fb-ecb18e1243f4" TYPE="xfs" 
/dev/sda2: UUID="pJ8unY-dS8y-vV14-YX2A-dFEg-WwST-TriV8T" TYPE="LVM2_member" 
/dev/mapper/centos-root: UUID="3295f8fa-8559-47a9-a5f7-0c092f3a04e1" TYPE="xfs" 
/dev/mapper/centos-swap: UUID="25b0bcea-10c9-4808-a75a-2f9626c05c66" TYPE="swap" 
/dev/mapper/centos-home: UUID="5ca451c5-f185-4a5c-a107-d2bc81a97392" TYPE="xfs" 
/dev/sdb: UUID="1d82c5ef-6439-4a98-9eda-eee42d88ecd4" TYPE="ext4" 
[root@localhost ~]# 
[root@localhost ~]# echo "UUID=1d82c5ef-6439-4a98-9eda-eee42d88ecd4 /Nfs_Disk ext4 defaults 0 0" >> /etc/fstab 
[root@localhost ~]# cat /etc/fstab 

#
# /etc/fstab
# Created by anaconda on Wed Jul  5 01:09:00 2023
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
/dev/mapper/centos-root /                       xfs     defaults        0 0
UUID=3ae6a4b1-0140-4d7d-b8fb-ecb18e1243f4 /boot                   xfs     defaults        0 0
/dev/mapper/centos-home /home                   xfs     defaults        0 0
/dev/mapper/centos-swap swap                    swap    defaults        0 0
UUID=1d82c5ef-6439-4a98-9eda-eee42d88ecd4 /Nfs_Disk ext4 defaults 0 0
[root@localhost ~]# 
[root@localhost ~]# mount -a
[root@localhost ~]# df -h
Filesystem               Size  Used Avail Use% Mounted on
devtmpfs                 894M     0  894M   0% /dev
tmpfs                    910M     0  910M   0% /dev/shm
tmpfs                    910M   11M  900M   2% /run
tmpfs                    910M     0  910M   0% /sys/fs/cgroup
/dev/mapper/centos-root   50G   20G   31G  39% /
/dev/sda1               1014M  185M  830M  19% /boot
/dev/mapper/centos-home  147G  135M  147G   1% /home
tmpfs                    182M  8.0K  182M   1% /run/user/42
tmpfs                    182M     0  182M   0% /run/user/0
/dev/sdb                  99G   61M   94G   1% /Nfs_Disk
[root@localhost ~]# 
```
#### 3/7 启动服务并进行挂载

```shell
## 7:启动服务并进行挂载
[root@localhost ~]# systemctl start nfs
[root@localhost ~]# systemctl status nfs
● nfs-server.service - NFS server and services
   Loaded: loaded (/usr/lib/systemd/system/nfs-server.service; disabled; vendor preset: disabled)
  Drop-In: /run/systemd/generator/nfs-server.service.d
           └─order-with-mounts.conf
   Active: active (exited) since Thu 2023-07-06 14:20:02 CST; 7s ago
  Process: 2373 ExecStartPost=/bin/sh -c if systemctl -q is-active gssproxy; then systemctl reload gssproxy ; fi (code=exited, status=0/SUCCESS)
  Process: 2357 ExecStart=/usr/sbin/rpc.nfsd $RPCNFSDARGS (code=exited, status=0/SUCCESS)
  Process: 2356 ExecStartPre=/usr/sbin/exportfs -r (code=exited, status=0/SUCCESS)
 Main PID: 2357 (code=exited, status=0/SUCCESS)
    Tasks: 0
   CGroup: /system.slice/nfs-server.service

Jul 06 14:20:02 localhost.localdomain systemd[1]: Starting NFS server and services...
Jul 06 14:20:02 localhost.localdomain systemd[1]: Started NFS server and services.
[root@localhost ~]# showmount -e 127.0.0.1
Export list for 127.0.0.1:
/Nfs_Disk 127.0.0.1/24
[root@localhost ~]# 
```
#### 3/8 授权

```shell
## 8:授权
--（也可以不授权这个和规划有关系，不授权后面的权限调整就可以不做）
[root@localhost /]# id nfsnobody
uid=65534(nfsnobody) gid=65534(nfsnobody) groups=65534(nfsnobody)
[root@localhost /]# chown -R nfsnobody.nfsnobody /Nfs_Disk
[root@localhost /]# cd Nfs_Disk/
[root@localhost Nfs_Disk]# mkdir test_mulu
[root@localhost Nfs_Disk]# touch test_file
[root@localhost Nfs_Disk]# echo 'test' >> test_file 
[root@localhost Nfs_Disk]# touch test_mulu/test2
[root@localhost Nfs_Disk]# echo 'test2' >> test_mulu/test2 
[root@localhost Nfs_Disk]# ll
total 24
drwx------ 2 nfsnobody nfsnobody 16384 Jul  6 14:15 lost+found
-rw-r--r-- 1 root      root          5 Jul  6 14:24 test_file
drwxr-xr-x 2 root      root       4096 Jul  6 14:24 test_mulu
```
#### 3/9 创建NFS协议挂载

```shell
## 9:创建NFS协议挂载
--（因为默认权限设置为rw,async所以创建出为ROOT权限，且走文件存储权限非NFS）
[root@localhost /]# mkdir NFS_LINK_DISK
[root@localhost /]# echo "127.0.0.1:/Nfs_Disk /NFS_LINK_DISK nfs defaults,_netdev 0 0" >> /etc/fstab 
[root@localhost /]# cat /etc/fstab 

#
# /etc/fstab
# Created by anaconda on Wed Jul  5 01:09:00 2023
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
/dev/mapper/centos-root /                       xfs     defaults        0 0
UUID=3ae6a4b1-0140-4d7d-b8fb-ecb18e1243f4 /boot                   xfs     defaults        0 0
/dev/mapper/centos-home /home                   xfs     defaults        0 0
/dev/mapper/centos-swap swap                    swap    defaults        0 0
UUID=1d82c5ef-6439-4a98-9eda-eee42d88ecd4 /Nfs_Disk ext4 defaults 0 0
127.0.0.1:/Nfs_Disk /NFS_LINK_DISK nfs defaults,_netdev 0 0
[root@localhost /]# mount -a
[root@localhost /]# df -h
Filesystem               Size  Used Avail Use% Mounted on
devtmpfs                 894M     0  894M   0% /dev
tmpfs                    910M     0  910M   0% /dev/shm
tmpfs                    910M   11M  900M   2% /run
tmpfs                    910M     0  910M   0% /sys/fs/cgroup
/dev/mapper/centos-root   50G   20G   31G  39% /
/dev/sda1               1014M  185M  830M  19% /boot
/dev/mapper/centos-home  147G  135M  147G   1% /home
tmpfs                    182M   12K  182M   1% /run/user/42
tmpfs                    182M     0  182M   0% /run/user/0
/dev/sdb                  99G   61M   94G   1% /Nfs_Disk
127.0.0.1:/Nfs_Disk       99G   60M   94G   1% /NFS_LINK_DISK
[root@localhost /]# 
```
#### 3/10 测试文件创建权限

```shell
## 10:测试文件创建权限
[root@localhost /]# cd /NFS_LINK_DISK/
[root@localhost NFS_LINK_DISK]# ls
lost+found  test_file  test_mulu
[root@localhost NFS_LINK_DISK]# ll
total 24
drwx------ 2 nfsnobody nfsnobody 16384 Jul  6 14:15 lost+found
-rw-r--r-- 1 root      root          5 Jul  6 14:24 test_file
drwxr-xr-x 2 root      root       4096 Jul  6 14:24 test_mulu
[root@localhost NFS_LINK_DISK]# mkdir test2_mulu
[root@localhost NFS_LINK_DISK]# touch test2_mulu/test3_file
[root@localhost NFS_LINK_DISK]# echo 'test3' >> test2_mulu/test3_file 
[root@localhost NFS_LINK_DISK]# ll
total 28
drwx------ 2 nfsnobody nfsnobody 16384 Jul  6 14:15 lost+found
drwxr-xr-x 2 nfsnobody nfsnobody  4096 Jul  6 14:34 test2_mulu
-rw-r--r-- 1 root      root          5 Jul  6 14:24 test_file
drwxr-xr-x 2 root      root       4096 Jul  6 14:24 test_mulu
[root@localhost NFS_LINK_DISK]# cd test2_mulu/
[root@localhost test2_mulu]# ll
total 4
-rw-r--r-- 1 nfsnobody nfsnobody 6 Jul  6 14:34 test3_file
[root@localhost test2_mulu]# 
```
#### 3/11 修改权限

```shell
## 11:修改权限
[root@localhost test2_mulu]# vim /etc/exports
[root@localhost test2_mulu]# cat /etc/exports
# /Nfs_Disk 127.0.0.1/24(rw,async)
/Nfs_Disk 127.0.0.1/24(rw,sync,root_squash)
[root@localhost test2_mulu]# 
权限说明：
rw 可读可写
sync 写入内存同时写入硬盘 保证数据不丢失 但是会导致IO增大
root_sqush 当NFS客户端以root管理员访问时，映射为NFS服务器的匿名用户（比较安全）
网络根据实际情况填写
/Nfs_Disk 为server主机对应的共享磁盘标识 为了保证数据一致性这里设置一个总的共享。
```
#### 3/12 重启服务使修改生效
```shell
## 12:重启服务使修改生效
[root@localhost test2_mulu]# systemctl restart nfs*
[root@localhost test2_mulu]# systemctl status nfs*
● nfs-mountd.service - NFS Mount Daemon
   Loaded: loaded (/usr/lib/systemd/system/nfs-mountd.service; static; vendor preset: disabled)
   Active: active (running) since Thu 2023-07-06 14:38:55 CST; 10s ago
  Process: 2746 ExecStart=/usr/sbin/rpc.mountd $RPCMOUNTDARGS (code=exited, status=0/SUCCESS)
 Main PID: 2748 (rpc.mountd)
    Tasks: 1
   CGroup: /system.slice/nfs-mountd.service
           └─2748 /usr/sbin/rpc.mountd

Jul 06 14:38:55 localhost.localdomain systemd[1]: Starting NFS Mount Daemon...
Jul 06 14:38:55 localhost.localdomain rpc.mountd[2748]: Version 1.3.0 starting
Jul 06 14:38:55 localhost.localdomain systemd[1]: Started NFS Mount Daemon.

● nfs-idmapd.service - NFSv4 ID-name mapping service
   Loaded: loaded (/usr/lib/systemd/system/nfs-idmapd.service; static; vendor preset: disabled)
   Active: active (running) since Thu 2023-07-06 14:38:55 CST; 10s ago
  Process: 2745 ExecStart=/usr/sbin/rpc.idmapd $RPCIDMAPDARGS (code=exited, status=0/SUCCESS)
 Main PID: 2747 (rpc.idmapd)
    Tasks: 1
   CGroup: /system.slice/nfs-idmapd.service
           └─2747 /usr/sbin/rpc.idmapd

Jul 06 14:38:55 localhost.localdomain systemd[1]: Starting NFSv4 ID-name mapping service...
Jul 06 14:38:55 localhost.localdomain systemd[1]: Started NFSv4 ID-name mapping service.

● nfs-server.service - NFS server and services
   Loaded: loaded (/usr/lib/systemd/system/nfs-server.service; disabled; vendor preset: disabled)
  Drop-In: /run/systemd/generator/nfs-server.service.d
           └─order-with-mounts.conf
   Active: active (exited) since Thu 2023-07-06 14:38:55 CST; 10s ago
  Process: 2738 ExecStopPost=/usr/sbin/exportfs -f (code=exited, status=0/SUCCESS)
  Process: 2733 ExecStopPost=/usr/sbin/exportfs -au (code=exited, status=0/SUCCESS)
  Process: 2730 ExecStop=/usr/sbin/rpc.nfsd 0 (code=exited, status=0/SUCCESS)
  Process: 2766 ExecStartPost=/bin/sh -c if systemctl -q is-active gssproxy; then systemctl reload gssproxy ; fi (code=exited, status=0/SUCCESS)
  Process: 2751 ExecStart=/usr/sbin/rpc.nfsd $RPCNFSDARGS (code=exited, status=0/SUCCESS)
  Process: 2749 ExecStartPre=/usr/sbin/exportfs -r (code=exited, status=0/SUCCESS)
 Main PID: 2751 (code=exited, status=0/SUCCESS)
    Tasks: 0
   CGroup: /system.slice/nfs-server.service

Jul 06 14:38:55 localhost.localdomain systemd[1]: Starting NFS server and services...
Jul 06 14:38:55 localhost.localdomain systemd[1]: Started NFS server and services.
[root@localhost test2_mulu]# 
```
> *-- > 进行到这里的时候MYSQLdump相关架构程序已经可以使用，请确保系统可以运行mysqldump测试方法执行mysqldump*，关于程序运行请跳转到-Ⅳ程序运行mysqldump部分

```shell
[root@localhost mysql]# mysqldump
Usage: mysqldump [OPTIONS] database [tables]
OR     mysqldump [OPTIONS] --databases [OPTIONS] DB1 [DB2 DB3...]
OR     mysqldump [OPTIONS] --all-databases [OPTIONS]
For more options, use mysqldump --help
[root@localhost mysql]# 
```

### 4. Mydumper 依赖安装

```shell
# 说明
--（项目lib文件夹中，mydumper-0.9.3-41.el7.x86_64.rpm 进行安装）
[root@localhost lib]# cd /root/IdeaProjects/Backup-tools/lib
[root@localhost lib]# rpm -qa | grep mydumper
[root@localhost lib]# rpm -ivh mydumper-0.9.3-41.el7.x86_64.rpm 
Preparing...                          ################################# [100%]
Updating / installing...
   1:mydumper-0.9.3-41                ################################# [100%]
[root@localhost lib]# rpm -qa | grep mydumper
mydumper-0.9.3-41.x86_64
[root@localhost lib]# mydumper
# 测试依赖
** (mydumper:5063): CRITICAL **: 13:58:22.089: Error connecting to database: Access denied for user 'root'@'localhost' (using password: NO)
[root@localhost lib]# 
```
> *-- > 进行到这里的时候MYdumper相关架构程序已经可以使用，请确保系统可以运行mydumper测试方法执行mydumper*，关于程序运行请跳转到-Ⅳ程序运行mydumper部分

### 5.xtrabackup 依赖安装

```shell
# 安装依赖
[root@localhost ~]# cd /root/IdeaProjects/Backup-tools/lib/
[root@localhost lib]# 
[root@localhost lib]# whereis innobackupex
innobackupex:[root@localhost lib]# innobackupex
bash: innobackupex: command not found...
[root@localhost lib]# 
[root@localhost lib]# rpm -ivh  percona-xtrabackup-*
warning: percona-xtrabackup-24-2.4.26-1.el7.x86_64.rpm: Header V4 RSA/SHA256 Signature, key ID 8507efa5: NOKEY
error: Failed dependencies:
        libev.so.4()(64bit) is needed by percona-xtrabackup-24-2.4.26-1.el7.x86_64
        perl(DBD::mysql) is needed by percona-xtrabackup-24-2.4.26-1.el7.x86_64
        perl(Digest::MD5) is needed by percona-xtrabackup-24-2.4.26-1.el7.x86_64
# 解决依赖冲突
[root@localhost lib]# cd /opt/soft/mysql_5.7.42
[root@localhost mysql_5.7.42]# rpm -ivh mysql-community-libs-compat-5.7.42-1.el7.x86_64.rpm
[root@localhost mysql_5.7.42]# yum install perl-DBD-MySQL
[root@localhost lib]# rpm -ivh percona-xtrabackup-*
warning: percona-xtrabackup-24-2.4.26-1.el7.x86_64.rpm: Header V4 RSA/SHA256 Signature, key ID 8507efa5: NOKEY
error: Failed dependencies:
        perl(Digest::MD5) is needed by percona-xtrabackup-24-2.4.26-1.el7.x86_64
[root@localhost lib]# 
[root@localhost lib]# yum install perl-Digest-MD5
# 安装成功，依赖解决每个系统不一样根据实际环境处理，最终RPM包安装成功即可。
[root@localhost lib]# rpm -ivh percona-xtrabackup-*
warning: percona-xtrabackup-24-2.4.26-1.el7.x86_64.rpm: Header V4 RSA/SHA256 Signature, key ID 8507efa5: NOKEY
Preparing...                          ################################# [100%]
Updating / installing...
   1:percona-xtrabackup-24-2.4.26-1.el################################# [ 33%]
   2:percona-xtrabackup-test-24-2.4.26################################# [ 67%]
   3:percona-xtrabackup-24-debuginfo-2################################# [100%]
[root@localhost lib]# 
# 测试
[root@localhost lib]# innobackupex
xtrabackup: recognized server arguments: --datadir=/data/mysql --log_bin=mysql-bin --server-id=1 
230710 13:30:24 innobackupex: Missing argument
[root@localhost lib]# 
```
> -- > 进行到这里的时候xtrabackup相关架构程序已经可以使用，请确保系统可以运行xtrabackup测试方法执行innobackupex，关于程序运行请跳转到-Ⅳ程序运行xtrabackup部分

## Ⅳ. 程序运行

### 1. Backup_Mysqldump_All

> 该程序为mysqldump原生的全库数据库备份程序。

#### 1/1 配置文件修改

```shell
## default_config
--（主程序配置）
NetworkSegment=127.0.0.1
--（监听网卡地址配置）
Date=$(date +%Y%m%d-%H%M%S)
--（日期参数）
Base_IP=$(ip addr | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}' | grep ${NetworkSegment})
--（获取IP参数配置）
Script_Dir=/root/IdeaProjects/Backup-tools/mysqldump
--（本程序绝对路径）
Script_Log=Backup_Mysqldump_All.log
--（程序生成日志文件名称）
Data_Storage_Save=/NFS_LINK_DISK/127.0.0.1/Mysqldump_Databases_All
--（备份文件生成文件路径配置）

## database_config
--（数据库程序配置）
MYSQL_Host=127.0.0.1
--（数据库主机地址）
MYSQL_Username=root
--（数据库用户名）
MYSQL_Password='A16&b36@@'
--（数据库密码）
MYSQL_Port=3306
--（数据库监听端口号）
MYSQL_Chara=default-character-set=utf8
--（数据库字符集）
MYSQL_Nfs_DiskDir="NFS_LINK_DISK"
--（数据库与NFS关联指针）
```

#### 1/2 程序启动

```shell
[root@localhost mysqldump]# cd /root/IdeaProjects/Backup-tools/mysqldump
[root@localhost mysqldump]# chmod +x Backup_Mysqldump_All.sh
[root@localhost mysqldump]# ./Backup_Mysqldump_All.sh 
mysqldump: [Warning] Using a password on the command line interface can be insecure.
```

#### 1/3 查看结果

```shell
# 文件查看
cd /NFS_LINK_DISK/127.0.0.1/Mysqldump_Databases_All
[root@localhost Mysqldump_Databases_All]# ll
total 576
-rw-r--r-- 1 nfsnobody nfsnobody 195751 Jul  7 10:10 20230707-101039-AllDatabases-backup.sql.gz
-rw-r--r-- 1 nfsnobody nfsnobody 195753 Jul  7 10:12 20230707-101244-AllDatabases-backup.sql.gz
-rw-r--r-- 1 nfsnobody nfsnobody 195753 Jul  7 10:28 20230707-102830-AllDatabases-backup.sql.gz
# 日志查看
[root@localhost mysqldump]# tail Backup_Mysqldump_All.log 
发现NFS挂载点 NFS_LINK_DISK，正在继续执行脚本……
正在判断是否有/NFS_LINK_DISK/127.0.0.1/Mysqldump_Databases_All,存储路径……
已发现存储路径/NFS_LINK_DISK/127.0.0.1/Mysqldump_Databases_All,正在继续执行……
正在执行备份……
备份开始时间:20230707-102830
备份方式:全库备份-mysqldump官方单线程
备份数据库IP:127.0.0.1
备份存储路径:/NFS_LINK_DISK/127.0.0.1/Mysqldump_Databases_All/对应时间-AllDatabases-backup.sql.gz
备份结束时间:20230707-102830
END 20230707-102830
[root@localhost mysqldump]# 
```

#### 1/4 结果说明

``` shell
# 用VIM 查看文件内容 （片段）
...
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='Database privileges';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `db`
--

LOCK TABLES `db` WRITE;
/*!40000 ALTER TABLE `db` DISABLE KEYS */;
INSERT INTO `db` VALUES ('localhost','performance_schema','mysql.session','Y','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N'),('localhost','sys','mysql.sys','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','Y');
/*!40000 ALTER TABLE `db` ENABLE KEYS */;
UNLOCK TABLES;
...

说明：程序执行为MySQL全量备份，输出的文件为全量的结构+数据一个的SQL文件且通过Gzip进行压缩后存储，满足预期。
```
### 2. Backup_Mysqldump_One

> 该程序为mysqldump原生的单个数据库备份程序。

#### 2/1 配置文件修改

```shell
## Default_config
NetworkSegment=127.0.0.1
Date=$(date +%Y%m%d-%H%M%S)
Base_IP=$(ip addr | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}' | grep ${NetworkSegment})
Script_Dir=/root/IdeaProjects/Backup-tools/mysqldump
Script_Log=Backup_Mysqldump_One.log
Data_Storage_Save=/NFS_LINK_DISK/127.0.0.1/Mysqldump_Save

## database_config
MYSQL_Host=1
MYSQL_Username=root
MYSQL_Password='A16&b36@@'
MYSQL_Port=3306
MYSQL_Chara=default-character-set=utf8
MYSQL_Database_Name=mysql
--（单个备份数据库名称）
MYSQL_Nfs_DiskDir="NFS_LINK_DISK"
```

#### 2/2 程序启动

```shell
[root@localhost mysqldump]# chmod +x Backup_Mysqldump_One.sh
[root@localhost mysqldump]# ./Backup_Mysqldump_One.sh 
mysqldump: [Warning] Using a password on the command line interface can be insecure.
[root@localhost mysqldump]# 
```

#### 2/3 查看结果

```SHELL
# 生成文件
[root@localhost 127.0.0.1]# tree
.
├── Mysqldump_Databases_All
│   ├── 20230707-101039-AllDatabases-backup.sql.gz
│   ├── 20230707-101244-AllDatabases-backup.sql.gz
│   └── 20230707-102830-AllDatabases-backup.sql.gz
└── Mysqldump_Save
    └── mysql
        └── 20230707-132623-mysql-backup.sql.gz

3 directories, 4 files
[root@localhost 127.0.0.1]# 

# 日志查看
[root@localhost mysqldump]# tail Backup_Mysqldump_One.log 
正在判断是否有对应数据库mysql,MYSQL_SAVE存储路径……
没有发现对应MYSQL_SAVE-mysql,对应数据库,正在创建……
正在执行备份……
备份开始时间:20230707-132623
备份方式:mysqldump官方单线程
备份数据库:mysql
备份数据库IP:127.0.0.1
备份存储路径:/NFS_LINK_DISK/127.0.0.1/Mysqldump_Save/mysql/对应时间-数据库名称-backup.sql.gz
备份结束时间:20230707-132623
END 20230707-132623
[root@localhost mysqldump]# 
```

#### 2/4 结果说明

``` shell
# 用VIM 查看文件内容 （片段）
...
-- Dumping data for table `db`
--

LOCK TABLES `db` WRITE;
/*!40000 ALTER TABLE `db` DISABLE KEYS */;
INSERT INTO `db` VALUES ('localhost','performance_schema','mysql.session','Y','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N'),('localhost','sys','mysql.sys','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','Y');
/*!40000 ALTER TABLE `db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engine_cost`
--

DROP TABLE IF EXISTS `engine_cost`;
...

说明：程序执行为MySQL单库备份，输出的文件为全量的结构+数据一个的SQL文件且通过Gzip进行压缩后存储，满足预期。
```

### 3. Backup_Mydumper_MultiThread_Database_All

> 该程序为多线程全量数据库备份程序

#### 3/1 配置文件修改

```shell
## Default_config
--（主要配置）
NetworkSegment=127.0.0.1
--（网络IP配置）
Date=$(date +%Y%m%d-%H%M%S)
--（日期格式配置）
Base_IP=$(ip addr | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}' | grep ${NetworkSegment})
--（IP获取配置）
Script_Dir=/root/IdeaProjects/Backup-tools/mydumper
--（脚本路劲配置）
Script_Log=Backup_Mydumper_MultiThread_Database_All.log
--（脚本日志配置）
Data_Storage_Save=/NFS_LINK_DISK/127.0.0.1/Mydumper_MultiThread_Databases_All
--（备份生成文件存储位置配置）

## Database_config
MYSQL_Host=127.0.0.1
--（数据库主机名）
MYSQL_Username=root
--（数据库账户名）
MYSQL_Password='A16&b36@@'
--（数据库密码）
MYSQL_Port=3306
--（数据库端口）
MYSQL_Chara=default-character-set=utf8
--（数据库字符集）
#MYSQL_Database_Name=sakila_b
MYSQL_Nfs_DiskDir="NFS_LINK_DISK"
--（数据库NFS指针）

# 是否开启压缩存储  压缩.SQL.GZ 占用空间小 不压缩.SQL 占用空间大
DUMPER_COMPERSS=-c
--（默认开启压缩）
# dumper信息展示级别,最详细级别
DUMPER_INFO_LAVEL=3
--（信息级别展示INFO）
# 备份线程数 根据实际情况调整
DUMPER_THREADS_NUMBER=32
--（备份线程数，根据主机实际情况）
# dumper信息展示存储日志位置
DUMPER_BACKINFO_LOG=${Script_Dir}/DUMPER_Backup_info.log
--（程序运行过程记录日志文件）
```

#### 3/2 程序启动

```shell
[root@localhost mydumper]# chmod +x Backup_Mydumper_MultiThread_Database_All.sh 
[root@localhost mydumper]# ./Backup_Mydumper_MultiThread_Database_All.sh 
[root@localhost mydumper]# tail DUMPER_Backup_info.log 
** Message: 14:10:34.013: Thread 21 shutting down
** Message: 14:10:34.017: Thread 20 shutting down
** Message: 14:10:34.019: Thread 18 shutting down
** Message: 14:10:34.024: Thread 5 shutting down
** Message: 14:10:34.025: Thread 1 shutting down
** Message: 14:10:34.032: Finished dump at: 2023-07-07 14:10:34
```

#### 3/3 查看结果

```SHELL
# 生成文件
[root@localhost mydumper]# cd /NFS_LINK_DISK/127.0.0.1/
[root@localhost 127.0.0.1]# tree
.
├── Mydumper_MultiThread_Databases_All
│   └── 20230707-141032-Databases-All
│       ├── metadata
│       ├── mysql.columns_priv-schema.sql.gz
│       ├── mysql.db-schema.sql.gz
```

#### 3/4 结果说明

``` shell
[root@localhost 20230707-141032-Databases-All]# vim mysql.proxies_priv.sql.gz
[root@localhost 20230707-141032-Databases-All]# ll | grep proxies
-rw-r--r-- 1 nfsnobody nfsnobody    338 Jul  7 14:10 mysql.proxies_priv-schema.sql.gz
-rw-r--r-- 1 nfsnobody nfsnobody    187 Jul  7 14:10 mysql.proxies_priv.sql.gz
[root@localhost 20230707-141032-Databases-All]# 

# 说明
可以看到全库多线程备份会在NFS路径下生成对应时间的文件夹并有schema结构文件，正常的数据文件，也就是会生成结构和数据分开的文件，满足预期。
```

### 4. Backup_Mydumper_MultiThread_Database_One

> 该程序为多线程单库全量数据库备份程序

#### 4/1 配置文件修改

```shell
MYSQL_Database_Name=sakila_b
--（其他配置和全量备份一致，只涉及数据库名称）
```

#### 4/2 程序启动

```shell
[root@localhost mydumper]# chmod +x Backup_Mydumper_MultiThread_Database_One.sh 
[root@localhost mydumper]# ./Backup_Mydumper_MultiThread_Database_One.sh 
```

#### 4/3 查看结果

```SHELL
# 文件结构
├── Mydumper_MultiThread_Save
│   └── mysql
│       └── 20230707-145056-mysql
│           ├── metadata
│           ├── mysql.columns_priv-schema.sql.gz
│           ├── mysql.db-schema.sql.gz
│           ├── mysql.db.sql.gz
```

#### 4/4 结果说明

``` shell
[root@localhost 20230707-145056-mysql]# ll | grep mysql.db
-rw-r--r-- 1 nfsnobody nfsnobody    405 Jul  7 14:50 mysql.db-schema.sql.gz
-rw-r--r-- 1 nfsnobody nfsnobody    200 Jul  7 14:50 mysql.db.sql.gz
[root@localhost 20230707-145056-mysql]# ll | grep -v mysql
total 384
-rw-r--r-- 1 nfsnobody nfsnobody    136 Jul  7 14:50 metadata
[root@localhost 20230707-145056-mysql]# 
# 说明
可以看到 此文件下只有mysql数据库得内容，包含结构和数据，其他数据库 grep -v mysql发现只有有个配置文件所以满足预期。
```

### 5. Backup_XtraBackup_add

> 该程序为XtraBackup增量备份程序，用于提供MySQL数据库的全量+增量备份程序

#### 5/1 配置文件修改

```shell
## Default_config
NetworkSegment=127.0.0.1
--（网络配置）
Date=$(date +%Y%m%d-%H%M%S)
--（日期设置）
Base_IP=$(ip addr | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}' | grep ${NetworkSegment})
--（网络配置参数）
Script_Dir=/root/IdeaProjects/Backup-tools/xtrabackup
--（脚本位置）
Script_Log=Backup_XtraBackup_Add.log
--（日志文件配置）
Data_Storage_Full=/NFS_LINK_DISK/127.0.0.1/XtraBackup/Full
--（全量备份存储位置）
Data_Storage_Add=/NFS_LINK_DISK/127.0.0.1/XtraBackup/Add
--（增量备份存储位置）

## Database_config
MYSQL_Username=root
--（数据库账户）
MYSQL_Password='A16&b36@@'
--（数据库密码）
MYSQL_Default=/etc/my.cnf
--（配置文件位置，需要判断binlog相关函数内容使用）
MYSQL_Port=3306
--（数据库端口）
MYSQL_Nfs_DiskDir="NFS_LINK_DISK"
--（NFS关联指针）
```

#### 5/2 程序启动

```shell
[root@localhost xtrabackup]# chmod +x Backup_XtraBackup_add.sh 
[root@localhost xtrabackup]# ll
total 8
-rwxr-xr-x 1 root root 4396 Jul 10 13:37 Backup_XtraBackup_add.sh
[root@localhost xtrabackup]# 
# 首次执行全量备份
[root@localhost xtrabackup]# ./Backup_XtraBackup_add.sh 
...
xtrabackup: The latest check point (for incremental): '2767189'
xtrabackup: Stopping log copying thread.
.230710 13:42:59 >> log scanned up to (2767198)

230710 13:42:59 Executing UNLOCK TABLES
230710 13:42:59 All tables unlocked
230710 13:42:59 [00] Copying ib_buffer_pool to /NFS_LINK_DISK/127.0.0.1/XtraBackup/Full/ib_buffer_pool
230710 13:42:59 [00]        ...done
230710 13:42:59 Backup created in directory '/NFS_LINK_DISK/127.0.0.1/XtraBackup/Full/'
MySQL binlog position: filename 'mysql-bin.000004', position '154'
230710 13:42:59 [00] Writing /NFS_LINK_DISK/127.0.0.1/XtraBackup/Full/backup-my.cnf
230710 13:42:59 [00]        ...done
230710 13:42:59 [00] Writing /NFS_LINK_DISK/127.0.0.1/XtraBackup/Full/xtrabackup_info
230710 13:42:59 [00]        ...done
xtrabackup: Transaction log of lsn (2767189) to (2767198) was copied.
230710 13:43:00 completed OK!
...
[root@localhost xtrabackup]# tail Backup_XtraBackup_Add.log 
START 20230710-134256
正在进行MySQL-binlog判断……
已发现mysqlbinlog相关配置，正在继续执行脚本……
发现NFS挂载点 NFS_LINK_DISK，正在继续执行脚本……
正在判断是否有FULL指针，请稍后……
没有找到全量备份FULL的指针，正在执行全量备份FULL
END 20230710-134256
```

#### 5/3 制作增量数据

```shell
# 读数据库进行查询、创建数据库、创建表、插入数据、查询操作
[root@localhost xtrabackup]# mysql -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 4
Server version: 5.7.42-log MySQL Community Server (GPL)

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.01 sec)

mysql> CREATE DATABASE menagerie;
Query OK, 1 row affected (0.01 sec)

mysql> CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20),species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);
ERROR 1046 (3D000): No database selected
mysql> use  menagerie;
Database changed
mysql> CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20),species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);
Query OK, 0 rows affected (0.05 sec)

mysql> SHOW TABLES;
+---------------------+
| Tables_in_menagerie |
+---------------------+
| pet                 |
+---------------------+
1 row in set (0.00 sec)

mysql> DESCRIBE pet;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| name    | varchar(20) | YES  |     | NULL    |       |
| owner   | varchar(20) | YES  |     | NULL    |       |
| species | varchar(20) | YES  |     | NULL    |       |
| sex     | char(1)     | YES  |     | NULL    |       |
| birth   | date        | YES  |     | NULL    |       |
| death   | date        | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
6 rows in set (0.01 sec)

mysql> INSERT INTO pet VALUES ('Puffball','Diane','hamster','f','1999-03-30',NULL);
Query OK, 1 row affected (0.00 sec)

mysql> select * from pet where name = 'Puffball';
+----------+-------+---------+------+------------+-------+
| name     | owner | species | sex  | birth      | death |
+----------+-------+---------+------+------------+-------+
| Puffball | Diane | hamster | f    | 1999-03-30 | NULL  |
+----------+-------+---------+------+------------+-------+
1 row in set (0.00 sec)

mysql> exit
Bye
# 查看binlog 是否记录 （片段）
[root@localhost mysql]# mysqlbinlog  -vv mysql-bin.000004
——> 可以看到创建数据库
CREATE DATABASE menagerie
/*!*/;
# at 328
#230710 13:53:24 server id 1  end_log_pos 393 CRC32 0x61986ec2  Anonymous_GTID  last_committed=1        sequence_number=2       rbr_only=no
SET @@SESSION.GTID_NEXT= 'ANONYMOUS'/*!*/;
# at 393
#230710 13:53:24 server id 1  end_log_pos 588 CRC32 0x9179e5d5  Query   thread_id=4     exec_time=0     error_code=0
use `menagerie`/*!*/;
SET TIMESTAMP=1688968404/*!*/;
CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20),species VARCHAR(20), sex CHAR(1), birth DATE, death DATE)
/*!*/;
——> 可以看到创建表并插入了数据
### INSERT INTO `menagerie`.`pet`
### SET
###   @1='Puffball' /* VARSTRING(20) meta=20 nullable=1 is_null=0 */
###   @2='Diane' /* VARSTRING(20) meta=20 nullable=1 is_null=0 */
###   @3='hamster' /* VARSTRING(20) meta=20 nullable=1 is_null=0 */
###   @4='f' /* STRING(1) meta=65025 nullable=1 is_null=0 */
###   @5='1999:03:30' /* DATE meta=0 nullable=1 is_null=0 */
###   @6=NULL /* DATE meta=0 nullable=1 is_null=1 */
# at 858
#230710 13:54:08 server id 1  end_log_pos 889 CRC32 0xcd0a44dd  Xid = 33
COMMIT/*!*/;
# at 889
#230710 14:02:55 server id 1  end_log_pos 912 CRC32 0x30331055  Stop
SET @@SESSION.GTID_NEXT= 'AUTOMATIC' /* added by mysqlbinlog */ /*!*/;
DELIMITER ;

```

#### 5/4 程序启动第N次

```shell
# 执行第二次启动并触发增量函数
[root@localhost xtrabackup]# ./Backup_XtraBackup_add.sh 
...
xtrabackup: The latest check point (for incremental): '2772290'
xtrabackup: Stopping log copying thread.
.230710 14:21:41 >> log scanned up to (2772299)

230710 14:21:41 Executing UNLOCK TABLES
230710 14:21:41 All tables unlocked
230710 14:21:41 [00] Copying ib_buffer_pool to /NFS_LINK_DISK/127.0.0.1/XtraBackup/Add/2023-07-10_14-21-37/ib_buffer_pool
230710 14:21:41 [00]        ...done
230710 14:21:41 Backup created in directory '/NFS_LINK_DISK/127.0.0.1/XtraBackup/Add/2023-07-10_14-21-37/'
MySQL binlog position: filename 'mysql-bin.000007', position '154'
230710 14:21:41 [00] Writing /NFS_LINK_DISK/127.0.0.1/XtraBackup/Add/2023-07-10_14-21-37/backup-my.cnf
230710 14:21:41 [00]        ...done
230710 14:21:41 [00] Writing /NFS_LINK_DISK/127.0.0.1/XtraBackup/Add/2023-07-10_14-21-37/xtrabackup_info
230710 14:21:41 [00]        ...done
xtrabackup: Transaction log of lsn (2772290) to (2772299) was copied.
230710 14:21:42 completed OK!
...
[root@localhost xtrabackup]# tail Backup_XtraBackup_Add.log 
END 20230710-134256
START 20230710-142137
正在进行MySQL-binlog判断……
已发现mysqlbinlog相关配置，正在继续执行脚本……
发现NFS挂载点 NFS_LINK_DISK，正在继续执行脚本……
正在判断是否有FULL指针，请稍后……
已经找到全量备份FULL的指针，正在执行增量判断，请稍后……
正在判断是否有增量ADD的指针，请稍后……
首次增量备份已完成
END 20230710-142137
[root@localhost xtrabackup]# 
```

#### 5/5 查看结果

```SHELL
# 首次执行全量备份查看文件
[root@localhost 127.0.0.1]# tree -L 2 XtraBackup/
XtraBackup/
└── Full
    ├── backup-my.cnf
    ├── ib_buffer_pool
    ├── ibdata1
    ├── mysql
    ├── performance_schema
    ├── sys
    ├── xtrabackup_binlog_info
    ├── xtrabackup_checkpoints
    ├── xtrabackup_info
    └── xtrabackup_logfile

4 directories, 7 files
[root@localhost 127.0.0.1]# pwd
/NFS_LINK_DISK/127.0.0.1
[root@localhost 127.0.0.1]# 
# 第二次执行增量备份查看文件
[root@localhost XtraBackup]# tree -L 2 .
.
├── Add
│   └── 2023-07-10_14-21-37
└── Full
    ├── backup-my.cnf
    ├── ib_buffer_pool
    ├── ibdata1
    ├── mysql
    ├── performance_schema
    ├── sys
    ├── xtrabackup_binlog_info
    ├── xtrabackup_checkpoints
    ├── xtrabackup_info
    └── xtrabackup_logfile

6 directories, 7 files
[root@localhost XtraBackup]# pwd
/NFS_LINK_DISK/127.0.0.1/XtraBackup
[root@localhost XtraBackup]# 
[root@localhost Add]# du -h .
1.1M    ./2023-07-10_14-21-37/performance_schema
1.2M    ./2023-07-10_14-21-37/mysql
104K    ./2023-07-10_14-21-37/menagerie
604K    ./2023-07-10_14-21-37/sys
3.4M    ./2023-07-10_14-21-37
3.4M    .
[root@localhost Add]# cd ..
[root@localhost XtraBackup]# ls
Add  Full
[root@localhost XtraBackup]# cd Full/
[root@localhost Full]# ls
backup-my.cnf  ib_buffer_pool  ibdata1  mysql  performance_schema  sys  xtrabackup_binlog_info  xtrabackup_checkpoints  xtrabackup_info  xtrabackup_logfile
[root@localhost Full]# du -h .
1.1M    ./performance_schema
12M     ./mysql
680K    ./sys
26M     .
[root@localhost Full]# 

```

#### 5/6 结果说明

```shell
[root@localhost Add]# du -h .
1.1M    ./2023-07-10_14-21-37/performance_schema
1.2M    ./2023-07-10_14-21-37/mysql
104K    ./2023-07-10_14-21-37/menagerie
604K    ./2023-07-10_14-21-37/sys
3.4M    ./2023-07-10_14-21-37
3.4M    .
[root@localhost Add]# cd ..
[root@localhost XtraBackup]# ls
Add  Full
[root@localhost XtraBackup]# cd Full/
[root@localhost Full]# ls
backup-my.cnf  ib_buffer_pool  ibdata1  mysql  performance_schema  sys  xtrabackup_binlog_info  xtrabackup_checkpoints  xtrabackup_info  xtrabackup_logfile
[root@localhost Full]# du -h .
1.1M    ./performance_schema
12M     ./mysql
680K    ./sys
26M     .
[root@localhost Full]# 
# 说明
可以看到 第一次程序执行获取了全量的mysql数据文件，存储在nfs的full位置上，第二次程序执行前进行了数据库操作，且重启了2次mysql，所以生成了2个全新的binlog文件，查询之前的binlog看到了相关的创建数据库、创建数据表相关操作，然后进行第二次程序执行，文件存储在nfs的add位置上，可以看到大小完全不一致，也就是说只存储了增量的数据，满足预期。
```

## Ⅴ. 开发

### 1. 构建开发环境

```shell
# GO环境搭建
[root@localhost soft]# wget https://go.dev/dl/go1.20.5.linux-amd64.tar.gz
[root@localhost soft]# tar xzvf go1.20.5.linux-amd64.tar.gz -C /usr/local/
[root@localhost go]# cd /usr/local/go/
[root@localhost go]# ll bin/go
-rwxr-xr-x 1 root root 15657886 Jun  2 01:04 bin/go
[root@localhost go]# bin/go version
go version go1.20.5 linux/amd64
[root@localhost go]# 
# 环境变量设置
[root@localhost go]# vim /etc/profile.d/go.sh
[root@localhost go]# cat /etc/profile.d/go.sh 
export GOROOT=/usr/local/go
export GOPATH=/root/go
export PATH=$PATH:$GOROOT/bin
[root@localhost go]# source /etc/profile
# 测试环境生效查看版本
[root@localhost go]# go version
go version go1.20.5 linux/amd64
[root@localhost go]# mkdir -p /root/go
[root@localhost go]# cd /root/go
[root@localhost go]# 
# 编译第一个程序
[root@localhost go]# vim hell.go
[root@localhost go]# cat hell.go 
package main
import "fmt"

func main(){
        fmt.Printf("Hello World")
}
[root@localhost go]# 
[root@localhost go]# go run hell.go 
Hello World[root@localhost go]# ls
hell.go  pkg
# 移动go程序
[root@localhost obj]# mv ~/go/hell.go .
[root@localhost obj]# ls
hell.go
# 初始化项目
[root@localhost obj]# go mod init example.com/hello
go: creating new go.mod: module example.com/hello
go: to add module requirements and sums:
        go mod tidy
[root@localhost obj]# ls
go.mod  hell.go
# 编译程序
[root@localhost obj]# go build hell.go 
[root@localhost obj]# ls
go.mod  hell  hell.go
[root@localhost obj]# ./hell 
Hello World[root@localhost obj]# 
--（至此环境测试成功）
```

### 2. 程序编译
```SHELL
  993  go mod init github.com/heike-07/Backup-tools
  994  go build
  995  go build Backup_Mydumper_MultiThread_Database_All.go
  996  go build Backup_Mydumper_MultiThread_Database_One.go
  997  go build Backup_Mysqldump_All.go
  998  go build Backup_Mysqldump_One.go
  999  go build Backup_XtraBackup_add.go

```
