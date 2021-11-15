#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Leona
# @time: 2020-06-17

from toolsForSE.userAndGroup import delUser,delUserGroup
from toolsForSE.share import delShare
from toolsForSE.snaps import delDiskSnap,delInstanceSnap,delPoolSnap
from toolsForSE.cloudDisk import delCloudDisk


def clearEnv():


    #清理用户、用户组
    delUser()
    delUserGroup()
    #清理共享
    delShare("883efa1d5a8e4932ad8df74495b3d4bf","%E9%BB%98%E8%AE%A4%E6%B1%A0")

    #清理业务池快照
    delPoolSnap()
    #清理云组件快照
    delInstanceSnap()
    #清理云硬盘快照
    delDiskSnap()

    #清理云硬盘
    delCloudDisk()

    print("*******************报告！~~测试数据清理完毕！**************************")

if __name__ == '__main__':
    clearEnv()