#!/bin/bash
# Title:: Backup_Mydumper_MultiThread_Database_One
# Author:: heike-07
# Description:: https://github.com/heike-07/Backup-tools.git
# Time:: 2022-04-18
# Update:: -

# Principle
# DATABASE(ONE) -> Mydumper -> SQL(...) -> SQL.gz(...)

# Config
#source /etc/profile
#source ~/.bash_profile

## Default_config
NetworkSegment=127.0.0.1
Date=$(date +%Y%m%d-%H%M%S)
Base_IP=$(ip addr | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}' | grep ${NetworkSegment})
Script_Dir=/root/IdeaProjects/Backup-tools/mydumper
Script_Log=Backup_Mydumper_MultiThread_Database_One.log
Data_Storage_Save=/NFS_LINK_DISK/127.0.0.1/Mydumper_MultiThread_Save

## Database_config
MYSQL_Host=127.0.0.1
MYSQL_Username=root
MYSQL_Password='A16&b36@@'
MYSQL_Port=3306
MYSQL_Chara=default-character-set=utf8
MYSQL_Database_Name=mysql
MYSQL_Nfs_DiskDir="NFS_LINK_DISK"

# 是否开启压缩存储  压缩.SQL.GZ 占用空间小 不压缩.SQL 占用空间大
DUMPER_COMPERSS=-c
# dumper信息展示级别,最详细级别
DUMPER_INFO_LAVEL=3
# 备份线程数 根据实际情况调整
DUMPER_THREADS_NUMBER=32
# dumper信息展示存储日志位置
DUMPER_BACKINFO_LOG=${Script_Dir}/DUMPER_Backup_info.log

If_NFS(){
    # Principle
    # IFIST NFS
    # df -h | grep NFS_LINK_DISK | awk '{print $6}'
    use_nfs_disk=$(df -h | grep NFS_LINK_DISK | awk '{print $6}' | sed 's/\///g')
    #echo use_nfs_disk $use_nfs_disk
    #echo MYSQL_Nfs_DiskDir $MYSQL_Nfs_DiskDir
    if [[ $MYSQL_Nfs_DiskDir == $use_nfs_disk  ]] ;then
        echo "发现NFS挂载点 $use_nfs_disk，正在继续执行脚本……"
        If_Save_Url
        else
        echo "脚本启动失败"
        echo "没有发现NFS挂载点，请先检查NFS挂载点 是否正确挂载到 $MYSQL_Nfs_DiskDir"
    fi

}

If_Mydumper(){
    # Principle
    # IFIST Mydumper
    # whereis mydumper | wc -l  Y=1  F=0
    mydumper_status=$(whereis mydumper | wc -l)
    if [[ $mydumper_status -eq 0 ]] ;then
	echo "没有发现mydumper程序,请确认该服务器是否为备份中控."
    	else
        echo "已发现mydumper程序,该服务器为备份中控服务器,正在执行拉取备份脚本……"
	If_NFS
    fi
}

If_Save_Url(){
    # Principle
    # if save_url isit?
    echo "正在判断是否有对应数据库$MYSQL_Database_Name,MYSQL_SAVE存储路径……"
    if [[ ! -d $Data_Storage_Save/$MYSQL_Database_Name ]] ;then
        echo "没有发现对应MYSQL_SAVE-$MYSQL_Database_Name,对应数据库文件夹,正在创建……"
        mkdir -p $Data_Storage_Save/$MYSQL_Database_Name
        Backup_One
        else
        echo "已发现对应数据库$MYSQL_Database_Name,MYSQL_SAVE存储路径,正在继续执行……"
        Backup_One
    fi
}

Backup_One(){
    # Principle
    # backupdatabae_one > save > sql.gz
    echo "正在执行备份……"
    echo "备份开始时间:$Date"
    echo "备份方式:mydumper多线程"
    echo "备份数据库:$MYSQL_Database_Name"
    echo "备份数据库IP:$MYSQL_Host"
    echo "备份存储路径:$Data_Storage_Save/$MYSQL_Database_Name/对应时间-数据库名称/XXX(...).sql.gz"
    #/usr/bin/mysqldump -u ${MYSQL_Username} -P ${MYSQL_Port} -p${MYSQL_Password} -h ${MYSQL_Host} --${MYSQL_Chara} ${MYSQL_Database_Name} | /usr/bin/gzip > $Data_Storage_Save/$MYSQL_Database_Name/$Date-$MYSQL_Database_Name-backup.sql.gz
    /usr/bin/nohup /usr/bin/mydumper -u ${MYSQL_Username} -p ${MYSQL_Password} -P ${MYSQL_Port} -h ${MYSQL_Host} -B ${MYSQL_Database_Name} ${DUMPER_COMPERSS} -v ${DUMPER_INFO_LAVEL} --threads ${DUMPER_THREADS_NUMBER} -o ${Data_Storage_Save}/${MYSQL_Database_Name}/$Date-${MYSQL_Database_Name} >> ${DUMPER_BACKINFO_LOG} 2>&1 &
   echo "备份结束时间:$Date"
}

# Main
cd $Script_Dir
echo START $Date >> $Script_Log
If_Mydumper >> $Script_Log
echo END $Date >> $Script_Log
