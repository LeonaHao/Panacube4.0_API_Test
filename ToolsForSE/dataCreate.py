#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Leona
# @time: 2020-06-17
import time
from ToolsForSE.Snaps import batchCreateVolume, createVolumeSnapShot
from ToolsForSE.cloudDisk import batchCreateCloudDisk, creCloudDiskSnapshot
from ToolsForSE.share import batchCreateShare
from ToolsForSE.userAndGroup import batchCreateUser,batchCreateUserGroup
from ToolsForSE.objectShare import batchCreateObjShare

def createData(n, poolId,num):
    #创建卷
    batchCreateVolume(n, poolId,num)
    time.sleep(5)
    #创建卷快照
    createVolumeSnapShot(poolId)
    #创建云硬盘
    batchCreateCloudDisk(n, poolId,num)
    time.sleep(5)
    #创建云硬盘快照
    creCloudDiskSnapshot(poolId)
    #创建共享
    batchCreateShare(n, poolId,num)
    #创建用户
    batchCreateUser(n, poolId,num)
    #创建用户组
    batchCreateUserGroup(n, poolId,num)
    #创建对象共享
    batchCreateObjShare(n, poolId,num)

    print("*******************哇哦~~测试数据构造完成喽！**************************")

#批量创建数据，createData(创建个数,'池id',名称开始的数值)
createData(3,'300',1)