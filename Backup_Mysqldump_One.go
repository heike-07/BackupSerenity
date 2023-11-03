package main

import (
	"fmt"
	"os/exec"
)

func main() {
	script := `
#!/bin/bash
# Title:: Backup_Mysqldump_One
# Author:: heike-07
# Description:: https://github.com/heike-07/Backup-tools.git
# Time:: 2022-04-18
# Update:: -

# Principle
# DATABASE(ONE) -> Mysqldump -> SQL -> SQL.gz

# Config
#source /etc/profile
#source ~/.bash_profile

# call Backup_Mysqldump_One
source conf/Backup_Mysqldump_One.conf

If_Docker(){
    # Principle
    # IFIST Is Docker
    # df -h | grep -e overlay | awk '{print $1}'
    # ll -a / | grep -e .dockerenv | awk '{print $9}'
    DockerType=$(df -h | grep -e overlay | awk '{print $1}')

    if [[ $DOCKER_TYPE == $DockerType ]] ;then
       echo "检测到/文件类型为overlay，判断为Docker容器环境"
       If_FOLDER
       else
       echo "没有检测到/文件类型为overlay，当前环境不是Docker容器环境"
       If_NFS
    fi

}

If_FOLDER(){
   # Principle
   # IFIST FOLDER NFS_LINK_DISK
   # ll -a / | grep -e NFS_LINK_DISK | awk '{print $9}'
   Folder=$(ls -la / | grep -e NFS_LINK_DISK | awk '{print $9}')

   if [[ $MYSQL_Nfs_DiskDir == $Folder ]] ;then
      echo "发现文件夹 $Folder，正在继续执行脚本……"
      If_Save_Url
      else
      echo "没有发现文件夹 $MYSQL_Nfs_DiskDir，请检查环境是否创建文件夹/$MYSQL_Nfs_DiskDir"
   fi
}

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
    echo "正在判断是否有对应数据库$MYSQL_Database_Name,MYSQL_SAVE存储路径……"
    if [[ ! -d $Data_Storage_Save/$MYSQL_Database_Name ]] ;then
	echo "没有发现对应MYSQL_SAVE-$MYSQL_Database_Name,对应数据库,正在创建……"
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
    echo "备份方式:mysqldump官方单线程"
    echo "备份数据库:$MYSQL_Database_Name"
    echo "备份数据库IP:$MYSQL_Host"
    echo "备份存储路径:$Data_Storage_Save/$MYSQL_Database_Name/对应时间-数据库名称-backup.sql.gz"
    /usr/bin/mysqldump -u ${MYSQL_Username} -P ${MYSQL_Port} -p${MYSQL_Password} -h ${MYSQL_Host} --${MYSQL_Chara} ${MYSQL_Database_Name} | /usr/bin/gzip > $Data_Storage_Save/$MYSQL_Database_Name/$Date-$MYSQL_Database_Name-backup.sql.gz
    echo "备份结束时间:$Date"
}

# Main
cd $Script_Dir
echo START $Date >> $Script_Log
If_Docker >> $Script_Log
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
