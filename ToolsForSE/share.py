#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Leona
# @time: 2020-06-16

import requests
import urllib3
from configs import urlConfigs
from lib.PanaCubeCommon import login





'''创建共享'''
def createShare(poolId,num):
    projectInfo = getProjectInfo()
    projectId = projectInfo[int(poolId)][0]
    projectName = projectInfo[int(poolId)][1]

    headers ={
        "Content-Type":"application/json",
        "Authorization": login(),
        "POOL-ID": poolId,
        "PROJECT-ID": projectId,
        "PROJECT-NAME": projectName

    }
    reqUrl = urlConfigs.shareUrl

    volumePathList = getVolumePathList(poolId)
    for volumePath in volumePathList:
        LV = volumePath.split('/',2)[2]
        reqParam = {
            "name":"share"+ str(num)+LV,
            "volume":volumePath,
            "cifs":"yes",
            "nfs":"yes",
            "browseable":"yes",
            "read_only":"no",
            "create_mask":"0744",
            "directory_mask":"0755",
            "guest_ok":"yes",
            "sync":"no",
            "no_root_squash":"yes"
        }
        print("请求参数是:  {}".format(reqParam))
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result = requests.post(url=reqUrl, headers=headers,json=reqParam,verify=False).json()
        print("响应结果是:  {}".format(result))
        if result['message']=='success':
            print("*******************成功创建共享**************************")
        else:
            print("*******************创建共享失败，响应结果为：{}".format(result))

'''批量共享'''
def batchCreateShare(n, poolId,num):
    for i in range(n):
        createShare(poolId,num)
        num = num + 1

'''获取共享列表'''
def getShareList(projectId,projectName):
    # projectInfo = getProjectInfo()
    # projectId = projectInfo[int(poolId)][0]
    # projectName = projectInfo[int(poolId)][1]

    headers ={
        "Content-Type":"application/json",
        "Authorization": login(),
        # "POOL-ID": poolId,
        "PROJECT-ID": projectId,
        "PROJECT-NAME": projectName

    }
    reqUrl = urlConfigs.shareUrl
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers,verify=False).json()
    # print("响应结果是:\n {}".format(result))
    if result['message']=='success':
        data = result['data']
        shareIdList = []

        if len(data) > 0:
            for i in range(len(data)):
                shareId = data[i]['id']
                shareIdList.append(shareId)

        print("获取的共享列表信息为：{}".format(shareIdList))
        return shareIdList

    else:
        print("*******************获取共享列表信息失败，响应结果为：{}".format(result))

'''删除共享列表'''
def delShare(projectId,projectName):
    # projectInfo = getProjectInfo()
    # projectId = projectInfo[int(poolId)][0]
    # projectName = projectInfo[int(poolId)][1]

    headers ={
        "Content-Type":"application/json",
        "Authorization": login(),
        # "POOL-ID": poolId,
        "PROJECT-ID": projectId,
        "PROJECT-NAME": projectName
    }

    shareIdList = getShareList(projectId,projectName)

    if len(shareIdList) > 0:
        reqUrl = urlConfigs.shareDelUrl
        reqParam = {
            "ids": shareIdList
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        shareDelRes = requests.delete(headers=headers,url=reqUrl,json=reqParam,verify=False).json()
        # print(shareDelRes)
        if shareDelRes['message'] == "success":
            print("*******************共享列表删除成功**************************")
        else:
            print("*******************共享列表删除失败,接口返回结果为：{}".format(shareDelRes))





# createShare("40",2)
# batchCreateShare(10,"676",1)
# getShareList("bd355250753e40c890c2e00472c5ce5a","%E9%BB%98%E8%AE%A4%E6%B1%A0")
# delShare("bd355250753e40c890c2e00472c5ce5a","%E9%BB%98%E8%AE%A4%E6%B1%A0")
