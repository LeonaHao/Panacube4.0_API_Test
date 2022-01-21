# -*- coding: utf-8 -*-
# @Time: 2021/11/17 10:12
# @Author: Leona
# @File: PanacubeCommonQuery.py

from lib.MySQLHelper import MySQLHelper
from lib.linuxXshell import conSSH
import time

#获取业务池信息
def getVolumeId():
    sql = 'select id, name, status,cpu_limit,memory_limit, storage_limit, gpu_limit, file_store_id,file_store_alloc,file_store_actual from cloud_pool;'
    param = ()
    res = MySQLHelper('panacube').get_many(sql,param)
    return res

#获取利用率信息
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


#获取任意一个非默认池
def getNonDefaultPool():
    sql = 'select id,name,storage_limit from cloud_pool WHERE type=1 order by create_time desc limit 1;'
    param = ()
    res= MySQLHelper('panacube').get_one(sql,param)
    return  res['id'],res['name'],res['storage_limit']


#获取可加载的数据盘信息
def getAttachableDisk(poolId):
    sql = 'select d.id as diskId, d.name as diskName, d.size as diskSize, d.status as diskStatus,\
             i.id as vmId, i.name as vmName, i.status as vmStatus, p.id as projectId, p.name as projectName \
             from  disk d LEFT JOIN cloud_instance i on i.project_id=d.pool_id INNER JOIN cloud_pool p on p.id=d.pool_id\
           where i.status in (1,3) and d.store_type=0 and d.status=1 and p.id=%s ORDER BY d.create_time desc limit 1;'
    param = (poolId)
    res= MySQLHelper('panacube').get_one(sql,param)
    return  res

#获取最新的数据盘id
def getLatestDataDisk(poolId):
    sql = 'select id from disk where store_type=0 and pool_id=%s order by create_time desc limit 1;'
    param = (poolId)
    res= MySQLHelper('panacube').get_one(sql,param)
    return  res

#获取最新的业务池快照
def getLatestPoolSnap(poolId):
    sql = 'SELECT snapshot_id, name from `storage_snapshot` WHERE snapshot_type="pool" and pool_id=%s order by create_time DESC limit 1;'
    param  = (poolId)
    res = MySQLHelper("panacube").get_one(sql,param)
    return res

#获取最新的数据盘快照
def getLatestDiskSnap(poolId):
    sql = 'SELECT id, snapshot_id, name, disk_id, pool_id from `storage_snapshot` WHERE snapshot_type="file" and pool_id=%s order by create_time DESC limit 1;'
    param  = (poolId)
    res = MySQLHelper("panacube").get_one(sql,param)
    return res

#获取最新的云组件快照
def getLatestInstanceSnap(poolId):
    sql = 'SELECT server_id, snapshot_name from `snapshot` WHERE project_id=%s order by create_time DESC limit 1; '
    param  = (poolId)
    res = MySQLHelper("panacube").get_one(sql,param)
    return res

#获取最新的云组件
def getLatestInstance(poolId):
    sql = 'SELECT id, name from `cloud_instance` WHERE project_id=%s order by create_time DESC limit 1 '
    param  = (poolId)
    res = MySQLHelper("panacube").get_one(sql,param)
    return res


#获取可创建云组件快照的云硬盘及组件信息
def getInsAndDisk(poolId):
    sql = 'SELECT i.id as vmId, i.name as vmName, d.id as diskId, d.name as diskName FROM cloud_instance i LEFT JOIN disk d on i.project_id=d.pool_id \
           where d.store_type=1 and i.project_id=%s limit 1;'
    param  = (poolId)
    res = MySQLHelper("panacube").get_one(sql,param)
    return res


#查询s3共享
def getS3():
    sql = 'SELECT id, name from cluster_share where s3=1;'
    param = ()
    res = MySQLHelper("panastor").get_one(sql,param)
    return res

#对比卷信息，排查问题时查看底层卷是否和db中的卷相一致，如果对比后发现有结果，则表示底层和db都存在
def matchVolume(hostname,port,username,password):
    volumes = getVolumeId()
    time.sleep(2)
    # logger.info("一共有{}个卷".format(len(volumes)))
    for i in range(len(volumes)):
        volumeId = volumes[i]['file_store_id'][:6]
        print("这是第{}个卷进行对比: ".format(i+1))
        cmd = 'gluster v info | grep '+ str(volumeId)
        conSSH(hostname,port,username,password,cmd)

# getVolumeId()
# matchVolume("192.168.5.174",22, "root","Admin@9000")
# getGeneralUsageInfo()
# getInstancesInPool("LeonaTestPool")
# getSysDiskUsageByNode()
# getNonDefaultPoolUsage('LeonaTestPool')
# getDefaultPoolUsage()
# getNonDefaultPool()
# getAttachableDisk()
# getLatestDataDisk('ddac080c671b473e885714538fd1ed6e')
# getLatestInstanceSnap('577d21c9411744a4b619c8966f69ec18')
# getLatestInstance('577d21c9411744a4b619c8966f69ec18')
# getInsAndDisk('63d8dd6776d848368ac817ed38cf93d6')


# print(type(getInsAndDisk("c732c22666064375904c357bbecfeb1a")))
# getLatestInstanceSnap("c732c22666064375904c357bbecfeb1a")
# getLatestDiskSnap("c732c22666064375904c357bbecfeb1a")
getS3()


