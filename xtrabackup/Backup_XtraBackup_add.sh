#!/bin/bash
# Title:: Backup_XtraBackup_Add
# Author:: heike-07
# Description:: https://github.com/heike-07/Backup-tools.git
# Time:: 2022-04-12
# Update:: 2022-04-14

# Principle
# ALL -> ADD1 -> ADD2 ...
# ADD ? 1:BASE ALL -> ADD1 2:BASE ADD1 -> ADD2

# Config
#source /etc/profile
#source ~/.bash_profile

## Default_config
NetworkSegment=127.0.0.1
Date=$(date +%Y%m%d-%H%M%S)
Base_IP=$(ip addr | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}' | grep ${NetworkSegment})
Script_Dir=/root/IdeaProjects/Backup-tools/xtrabackup
Script_Log=Backup_XtraBackup_Add.log
Data_Storage_Full=/NFS_LINK_DISK/127.0.0.1/XtraBackup/Full
Data_Storage_Add=/NFS_LINK_DISK/127.0.0.1/XtraBackup/Add

## Database_config
MYSQL_Username=root
MYSQL_Password='A16&b36@@'
MYSQL_Default=/etc/my.cnf
MYSQL_Port=3306
MYSQL_Nfs_DiskDir="NFS_LINK_DISK"

# Function
XtraBackup_Full(){
    # Principle
    # ALL
    /usr/bin/innobackupex --defaults=$MYSQL_Default --no-timestamp --port=$MYSQL_Port --user=$MYSQL_Username --password=$MYSQL_Password $Data_Storage_Full
}
XtraBackup_If(){
    # Principle
    # IF FULL isit -> ADD
    echo "正在判断是否有FULL指针，请稍后……"
    if [[ ! -d $Data_Storage_Full ]] ;then
	# 不存在为真
	echo "没有找到全量备份FULL的指针，正在执行全量备份FULL"
	mkdir -p $Data_Storage_Full
        XtraBackup_Full
	else
	# 存在为假
	echo "已经找到全量备份FULL的指针，正在执行增量判断，请稍后……"
	XtraBackup_Add
    fi

}

XtraBackup_Add(){
     # Principle
     # ADD
     # ls -l | grep ZL | sort | awk 'NR==1 {print $9}'  获取ZL开头的最新的日期排序。
     echo "正在判断是否有增量ADD的指针，请稍后……"
     if [[ ! -d $Data_Storage_Add ]] ;then
	mkdir -p $Data_Storage_Add
	# innobackupex --defaults-file=/etc/mcnf --user=root --password='A16&@' --incremental --incremental-basedir=/backup/2021-2/ /backup/zenliang/
	/usr/bin/innobackupex --defaults=$MYSQL_Default --port=$MYSQL_Port --user=$MYSQL_Username --password=$MYSQL_Password --incremental --incremental-basedir=$Data_Storage_Full $Data_Storage_Add
     	echo "首次增量备份已完成"
	else
	XtraBackup_Add_N
     fi

}

XtraBackup_Add_N(){
     # Principle
     # ADD * N
     # ls -l | grep -v total | wc -l
     add_number=$(ls -l $Data_Storage_Add | grep -v total | wc -l)
     if [[ $add_number -eq 0 ]] ;then
	echo "不可能出现的情况"
     	else
	echo "正在执行第N次增量备份……"
	add_file=$(ls -l $Data_Storage_Add | sort -r | grep -v total | awk 'NR==1 {print $9}')
	/usr/bin/innobackupex --defaults=$MYSQL_Default --port=$MYSQL_Port --user=$MYSQL_Username --password=$MYSQL_Password --incremental --incremental-basedir=$Data_Storage_Add/$add_file $Data_Storage_Add
	echo "第N次增量备份已完成"
     fi
}

XtraBackup_If_NFS(){
    # Principle
    # IFIST NFS
    # df -h | grep NFS_LINK_DISK | awk '{print $6}'
    use_nfs_disk=$(df -h | grep NFS_LINK_DISK | awk '{print $6}' | sed 's/\///g')
    #echo use_nfs_disk $use_nfs_disk
    #echo MYSQL_Nfs_DiskDir $MYSQL_Nfs_DiskDir
    if [[ $MYSQL_Nfs_DiskDir == $use_nfs_disk  ]] ;then
	echo "发现NFS挂载点 $use_nfs_disk，正在继续执行脚本……"
	XtraBackup_If
    	else
	echo "脚本启动失败"
        echo "没有发现NFS挂载点，请先检查NFS挂载点 是否正确挂载到 $MYSQL_Nfs_DiskDir"
    fi

}
Mysql_binlog_If(){
    # Principle
    # 要满足2个条件：
    # mysql配置中必须含有binlog：1. cat /etc/my.cnf | grep bin | grep -v '#' | wc -l   >=1
    # mysql配置中必须含有serverid：2. cat /etc/my.cnf | grep server-id | grep -v '#' | wc -l  >=1
    echo "正在进行MySQL-binlog判断……"
    mysql_binlog_num=$(cat $MYSQL_Default | grep bin | grep -v '#' | wc -l)
    mysql_serverid_num=$(cat $MYSQL_Default | grep server-id | grep -v '#' | wc -l)
    if [[ mysql_binlog_num -ge 1 ]] && [[ mysql_serverid_num -ge 1 ]] ;then
	#echo $mysql_binlog_num $mysql_serverid_num
	echo "已发现mysqlbinlog相关配置，正在继续执行脚本……"
	XtraBackup_If_NFS
    	else
	echo "脚本启动失败"
        echo "配置文件$MYSQL_Default，中没有binlog相关配置，请先修改相关配置并重启数据库再次尝试。"
    fi
}

# Main
cd $Script_Dir
echo START $Date >> $Script_Log
Mysql_binlog_If >> $Script_Log
echo END $Date >> $Script_Log
