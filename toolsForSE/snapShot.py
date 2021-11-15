#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Leona
# @time: 2020-06-15


import requests
import urllib3
from configs import urlConfigs
from lib.PanaCubeCommon import login,  getProjectInfo

'''获取云硬盘快照列表'''
def getCloudDiskSnapshot(poolId):
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

    reqUrl = urlConfigs.cloudDiskSnapshot
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers,verify=False).json()

    if result['message'] == 'success':
        data = result['data']
        data_disks = data['data_disks']
        sys_disks = data['sys_disks']

        dataDiskSnapList = []
        sysDiskSnapList = []

        if len(data_disks) > 0:
            for i in range(len(data_disks)):
                dataSnapId = data_disks[i]['id']
                dataDiskSnapList.append(dataSnapId)

        if len(sys_disks) > 0:
            for j in range(len(sys_disks)):
                sysSbaokId = sys_disks[j]['id']
                sysDiskSnapList.append(sysSbaokId)

        print("获取的数据盘快照列表信息为：{}".format(dataDiskSnapList))
        print("获取的系统盘快照列表信息为：{}".format(sysDiskSnapList))
        return dataDiskSnapList, sysDiskSnapList

    else:
        print("*******************获取云硬盘快照列表信息失败，响应结果为：{}".format(result))


'''删除云硬盘快照列表'''
def delCloudDiskSnapshot(poolId):

    projectInfo = getProjectInfo()
    projectId = projectInfo[int(poolId)][0]
    projectName = projectInfo[int(poolId)][1]
    dataDiskSnapList, sysDiskSnapList = getCloudDiskSnapshot(poolId)
    headers ={
        "Content-Type":"application/json",
        "Authorization": login(),
        "POOL-ID": poolId,
        "PROJECT-ID": projectId,
        "PROJECT-NAME": projectName

    }

    if len(dataDiskSnapList) > 0:
        reqUrl = urlConfigs.batchDeleteSnapshot
        # print(reqUrl)
        reqParam = {
            "ids": dataDiskSnapList
        }
        # print(reqParam)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result = requests.post(url=reqUrl, headers=headers, json=reqParam, verify=False).json()
        if result['message'] == "success":
            print("*******************数据盘快照删除成功**************************")
        else:
            print("*******************数据盘快照删除失败,接口返回结果为：{}".format(result))

    if len(sysDiskSnapList) > 0:
        reqUrl = urlConfigs.batchDeleteSnapshot
        # print(reqUrl)
        reqParam = {
            "ids": sysDiskSnapList
        }
        # print(reqParam)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result = requests.post(url=reqUrl, headers=headers, json=reqParam, verify=False).json()
        if result['message'] == "success":
            print("*******************系统盘快照删除成功**************************")
        else:
            print("*******************系统盘快照删除失败,接口返回结果为：{}".format(result))



# getCloudDiskSnapshot("5")
# delCloudDiskSnapshot("517")
