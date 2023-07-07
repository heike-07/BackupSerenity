#!/bin/bash
# Title:: Backup_Mysqldump_All
# Author:: heike-07
# Description:: https://github.com/heike-07/Backup-tools.git
# Time:: 2022-04-18
# Update:: -
# Principle
# DATABASE(ALL) -> Mysqldump -> SQL -> SQL.gz

# Config
#source /etc/profile
#source ~/.bash_profile

## Default_config
NetworkSegment=127.0.0.1
Date=$(date +%Y%m%d-%H%M%S)
Base_IP=$(ip addr | awk '/^[0-9]+: / {}; /inet.*global/ {print gensub(/(.*)\/(.*)/, "\\1", "g", $2)}' | grep ${NetworkSegment})
Script_Dir=/root/IdeaProjects/Backup-tools/mysqldump
Script_Log=Backup_Mysqldump_All.log
Data_Storage_Save=/NFS_LINK_DISK/127.0.0.1/Mysqldump_Databases_All

## Database_config
MYSQL_Host=127.0.0.1
MYSQL_Username=root
MYSQL_Password='A16&b36@@'
MYSQL_Port=3306
MYSQL_Chara=default-character-set=utf8
MYSQL_Nfs_DiskDir="NFS_LINK_DISK"

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

If_Save_Url(){
    # Principle
    # if save_url isit?
    echo "正在判断是否有$Data_Storage_Save,存储路径……"
    if [[ ! -d $Data_Storage_Save ]] ;then
	echo "没有找到存储路径$Data_Storage_Save,正在创建……"
	mkdir -p $Data_Storage_Save
        Backup_All
    	else
	echo "已发现存储路径$Data_Storage_Save,正在继续执行……"
        Backup_All
    fi
}

Backup_All(){
    # Principle
    # backupdatabae_one > save > sql.gz
    echo "正在执行备份……"
    echo "备份开始时间:$Date"
    echo "备份方式:全库备份-mysqldump官方单线程"
    echo "备份数据库IP:$MYSQL_Host"
    echo "备份存储路径:$Data_Storage_Save/对应时间-AllDatabases-backup.sql.gz"
    /usr/bin/mysqldump --all-databases -u ${MYSQL_Username} -P ${MYSQL_Port} -p${MYSQL_Password} -h ${MYSQL_Host} --${MYSQL_Chara} | /usr/bin/gzip > $Data_Storage_Save/$Date-AllDatabases-backup.sql.gz
    echo "备份结束时间:$Date"
}

# Main
cd $Script_Dir
echo START $Date >> $Script_Log
If_NFS >> $Script_Log
echo END $Date >> $Script_Log
