# Backup-tools

## 程序说明
一个更高效、更方便的MySQL数据库备份工具

## 开发任务
1. _`OK`_ - 思路建设 

## 底层环境构建
### 1. 操作系统适用
适用于Centos7、Redhat7 操作系统，其他系统适配中……
### 2. mysql或mariadb数据库
需要能访问到本机的数据库端口以及IP即可，例如127.0.0.1，3306

```shell
# 参考安装
--（因为本机为实验环境没有MySQL则需要安装）
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
## 2:检查mariadb依赖 
--（默认安装的系统都有）
[root@localhost mysql_5.7.42]# rpm -qa | grep mariadb
mariadb-libs-5.5.68-1.el7.x86_64
[root@localhost mysql_5.7.42]# rpm -e --nodeps mariadb-libs-5.5.68-1.el7.x86_64
[root@localhost mysql_5.7.42]# rpm -qa | grep mariadb
[root@localhost mysql_5.7.42]# 
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
default-character-set=utf8
socket=/data/mysql/mysql.sock

[mysql]
default-character-set=utf8
socket=/data/mysql/mysql.sock
[root@localhost mysql_5.7.42]# 
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

```shell
# 查询相关服务
[root@localhost ~]# systemctl status nfs*
如果没有则需要安装
# 环境安装
## 1:SELiunx 关闭
[root@localhost ~]# getsebool 
getsebool:  SELinux is disabled
## 2:安装NFS
[root@localhost ~]# yum install nfs-utils
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
## 5:创建路径编写可读可写权限
[root@localhost ~]# mkdir /Nfs_Disk
[root@localhost ~]# echo "/Nfs_Disk 127.0.0.1/24(rw,async)" >> /etc/exports
[root@localhost ~]# cat /etc/exports
/Nfs_Disk 127.0.0.1/24(rw,async)
[root@localhost ~]# 
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

> *-- > 进行到这里的时候MYSQLdump相关架构已经可以使用，请确保系统可以运行mysqldump测试方法执行mysqldump*

```shell
[root@localhost mysql]# mysqldump
Usage: mysqldump [OPTIONS] database [tables]
OR     mysqldump [OPTIONS] --databases [OPTIONS] DB1 [DB2 DB3...]
OR     mysqldump [OPTIONS] --all-databases [OPTIONS]
For more options, use mysqldump --help
[root@localhost mysql]# 
```