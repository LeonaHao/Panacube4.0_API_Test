# -*- coding: utf-8 -*-
# @Time: 2021/11/17 10:12
# @Author: Leona
# @File: PanacubeCommonQuery.py

from lib.MySQLHelper import MySQLHelper
from lib.linuxXshell import conSSH
from lib.log import logger
import time

def getVolumeId():
    sql = 'select id, name, status,cpu_limit,memory_limit, storage_limit, gpu_limit, file_store_id,file_store_alloc,file_store_actual from cloud_pool;'
    param = ()
    res = MySQLHelper('panacube').get_many(sql,param)
    return res

def matchVolume(hostname,port,username,password):
    volumes = getVolumeId()
    time.sleep(2)
    # logger.info("一共有{}个卷".format(len(volumes)))
    for i in range(len(volumes)):
        volumeId = volumes[i]['file_store_id'][:6]
        print("这是第{}个卷进行对比: ".format(i+1))
        cmd = 'gluster v info | grep '+ str(volumeId)
        conSSH(hostname,port,username,password,cmd)

def getGeneralUsageInfo():
    sql = 'SELECT sum(cpu_limit) as cpuUse, sum(memory_limit)/1024 as memUse, sum(file_store_alloc)/1024 as storageUse from cloud_pool;'
    param = ()
    res = MySQLHelper('panacube').get_one(sql,param)
    return res

#查询某一业务池下的所有组件
def getInstancesInPool(poolName):
    sql = 'SELECT * FROM cloud_instance WHERE project_id=(select id from cloud_pool where name =%s)'
    param =(poolName)
    res = MySQLHelper('panacube').get_many(sql,param)
    return res


#查询创建业务池时，各个节点的系统盘已使用空间
def getSysDiskUsageByNode():
    sql = 'SELECT location as Node, sum(size) as sysUsage from cloud_instance GROUP BY location;'
    param =()
    res = MySQLHelper('panacube').get_one(sql,param)
    return res

#非默认池的利用率=云硬盘使用值/文件空间配额
def getNonDefaultPoolUsage(poolName):
    sql = 'SELECT sum(d.size)/cp.file_store_alloc as poolUsage from disk d INNER JOIN cloud_pool cp ON d.pool_id=cp.id WHERE cp.name= %s and d.store_type=0;'
    param =(poolName)
    res = MySQLHelper('panacube').get_one(sql,param)
    return res

#默认池的利用率=云硬盘使用值/文件空间配额
def getDefaultPoolUsage():
    sql = 'SELECT sum(d.size)/cp.file_store_alloc as defaultPoolUsage from disk d INNER JOIN cloud_pool cp ON d.pool_id=cp.id WHERE cp.type=0;'
    param =()
    res = MySQLHelper('panacube').get_one(sql,param)
    return res




# getVolumeId()
# matchVolume("192.168.5.174",22, "root","Admin@9000")
# getGeneralUsageInfo()
# getInstancesInPool("LeonaTestPool")
# getSysDiskUsageByNode()
# getNonDefaultPoolUsage('LeonaTestPool')
# getDefaultPoolUsage()