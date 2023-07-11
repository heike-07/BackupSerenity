package main

import (
	"fmt"
	"os/exec"
)

func main() {
	script := `
#!/bin/bash
# Title:: Backup_Mydumper_MultiThread_Database_All
# Author:: heike-07
# Description:: https://github.com/heike-07/Backup-tools.git
# Time:: 2022-04-18
# Update:: -

# Principle
# DATABASE(ALL) -> Mydumper -> SQL(...) -> SQL.gz(...)

# CALL Backup_Mydumper_MultiThread_Database_All.conf
source conf/Backup_Mydumper_MultiThread_Database_All.conf

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
    echo "正在判断是否有对应全库存储路径$Data_Storage_Save"
    if [[ ! -d $Data_Storage_Save ]] ;then
        echo "没有发现对应$Data_Storage_Save,全库存储路径,正在创建……"
        mkdir -p $Data_Storage_Save
        Backup_All
        else
        echo "已发现对应$Data_Storage_Save,全库存储路径,正在继续执行……"
        Backup_All
    fi
}

Backup_All(){
    # Principle
    # backupdatabae_one > save > sql.gz
    echo "正在执行备份……"
    echo "备份开始时间:$Date"
    echo "备份方式:mydumper多线程-全库备份"
    #echo "备份数据库:$MYSQL_Database_Name"
    echo "备份数据库IP:$MYSQL_Host"
    echo "备份存储路径:$Data_Storage_Save/对应时间-Databases-All/XXX(...).sql.gz"
    #/usr/bin/mysqldump -u ${MYSQL_Username} -P ${MYSQL_Port} -p${MYSQL_Password} -h ${MYSQL_Host} --${MYSQL_Chara} ${MYSQL_Database_Name} | /usr/bin/gzip > $Data_Storage_Save/$MYSQL_Database_Name/$Date-$MYSQL_Database_Name-backup.sql.gz
    /usr/bin/nohup /usr/bin/mydumper -u ${MYSQL_Username} -p ${MYSQL_Password} -P ${MYSQL_Port} -h ${MYSQL_Host} ${DUMPER_COMPERSS} -v ${DUMPER_INFO_LAVEL} --threads ${DUMPER_THREADS_NUMBER} -o ${Data_Storage_Save}/$Date-Databases-All >> ${DUMPER_BACKINFO_LOG} 2>&1 &
   echo "备份结束时间:$Date"
}

# Main
cd $Script_Dir
echo START $Date >> $Script_Log
If_Mydumper >> $Script_Log
echo END $Date >> $Script_Log

`
	cmd := exec.Command("sh", "-c", script)
	output, err := cmd.Output()
	if err != nil {
		fmt.Print("error...", err)
		return
	}
	fmt.Print(string(output))
}
