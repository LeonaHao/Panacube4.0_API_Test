#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Leona
# @time: 2020-05-26

import requests
import urllib3
import random
from configs import urlConfigs
from lib.PanaCubeCommon import login
from ToolsForSE.Snaps import delDiskSnap


Token = login()

'''创建云硬盘'''
def createCloudDisk(num,projectId, projectName):
    try:
        headers ={
            "Content-Type":"application/json",
            "Authorization": Token,
        }
        reqUrl = urlConfigs.cloudDisk
        reqParam = {
            "name":"CloudDisk" + str(num),
            "size":"1",
            "disk_type": 0,
            "description": "",
            "compression": "off",
            "dedup": "off",
            "volblocksize": "512B",
            "share_vol": 1,
            "project_id": projectId,
            "project_name": projectName

        }
        print("请求参数是:  {}".format(reqParam))
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result = requests.post(url=reqUrl, headers=headers,json=reqParam,verify=False).json()
        print("响应结果是:  {}".format(result))
        if result['message']=='success':
            print("*******************成功创建云硬盘**************************")
        else:
            print("*******************创建云硬盘失败，响应结果为：{}".format(result))
    except Exception as e:
        print(e)

'''批量创建云硬盘'''
def batchCreateCloudDisk(n, num, projectId,projectName,):
    for i in range(n):
        createCloudDisk(num,projectId,projectName)
        num = num + 1

'''获取云硬盘id列表'''
def getCloudDiskList():
    headers ={
        "Content-Type":"application/json",
        "Authorization": Token
    }
    reqUrl = urlConfigs.cloudDisk + "?info=data"
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers,verify=False).json()
    # print("响应结果是:\n {}".format(result))
    if result['message']=='success':
        data = result['data']
        dataDiskList = {}
        if len(data) > 0:
            print("共有{}个数据盘".format(len(data)))
            for i in range(len(data)):
                dataDiskList[data[i]['name']]=(data[i]['id'],data[i]['disk_status'],data[i]['is_snapshoted'])
        else:
            print("数据盘列表为空")

        print("获取的数据盘列表信息为：{}".format(dataDiskList))
        return dataDiskList

    else:
        print("*******************获取云硬盘信息失败，响应结果为：{}".format(result))




'''删除数据盘、缓存盘, 删除前要确保数据盘未挂载'''
def delCloudDisk():

    headers ={
        "Content-Type":"application/json",
        "Authorization": Token
    }

    dataDiskList = getCloudDiskList()

    for diskName,diskInfo in dataDiskList.items():
        '''如果云硬盘已挂载，则先卸载云硬盘'''
        if diskInfo[1] == 0:
            '''获取云硬盘加载的云组件'''
            reqAttachUrl = urlConfigs.cloudDisk + '/' + diskInfo[0]
            instanceInfo = requests.get(url=reqAttachUrl, headers=headers, verify=False).json()
            instanceId = instanceInfo['data']['used_by'][0]['id']
            '''卸载云硬盘'''
            detachParam = {
                "instance":[
                    instanceId
                ],
                "action":"detach",
                "volume":diskInfo[0]
            }
            detachResult = requests.post(headers=headers,url=urlConfigs.cloudDiskDetach,json=detachParam,verify=False).json()
            if detachResult['message'] == 'success':
                print("*******************云硬盘卸载成功**************************")
            else:
                print("*******************云硬盘卸载失败**************************")

        elif diskInfo[2] == 0:
            '''如果云硬盘有快照，先删除快照'''
            delDiskSnap()

        '''删除云硬盘'''
        reqDelDiskUrl = urlConfigs.batchDeleteCloudDisk
        reqDelDiskParam = {
            "disk_ids":[diskInfo[0]]
        }
        delDiskResult = requests.post(headers=headers,url=reqDelDiskUrl, json=reqDelDiskParam, verify=False).json()
        if delDiskResult['message'] == 'success':
            print("*******************云硬盘{}删除成功**************************".format(diskName))
        else:
            print("*******************云硬盘{}删除失败**************************".format(diskName))


    # if len(dataDiskList) > 0:
    #     for i in range(len(dataDiskList)):
    #
    #         if
    #         dataDiskList[i] ='id=' + dataDiskList[i] + '&'
    #     dataParam = '?' + ''.join(dataDiskList) + 'force=false'
    #     reqUrl = urlConfigs.cloudDisk+dataParam
    #     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #     dataDelRes = requests.delete(headers=headers,url=reqUrl,verify=False).json()
    #     print(dataDelRes)
    #     if dataDelRes['message'] == "success":
    #         print("*******************数据盘列表删除成功**************************")
    #     else:
    #         print("*******************数据盘列表删除失败,接口返回结果为：{}".format(dataDelRes))

    # if len(sysDiskLIst) > 0:
    #     for i in range(len(sysDiskLIst)):
    #         sysDiskLIst[i] = 'id=' + sysDiskLIst[i] + '&'
    #     sysParam = '?' + ''.join(sysDiskLIst) + 'force=false'
    #     reqUrl = urlConfigs.cloudDisk+sysParam
    #     print(reqUrl)
    #     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #     sysDelRes = requests.delete(headers=headers,url=reqUrl,verify=False).json()
    #     if sysDelRes['message'] == "success":
    #         print("*******************系统盘列表删除成功**************************")
    #     else:
    #         print("*******************系统盘列表删除失败,接口返回结果为：{}".format(sysDelRes))

    # if len(cacheDiskList) > 0:
    #     for i in range(len(cacheDiskList)):
    #         cacheDiskList[i] = 'id=' + cacheDiskList[i] + '&'
    #     cacheParam = '?' + ''.join(cacheDiskList) + 'force=false'
    #     reqUrl = urlConfigs.cloudDisk + cacheParam
    #     print(reqUrl)
    #     urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #     cacheDelRes = requests.delete(headers=headers,url=reqUrl,verify=False).json()
    #     if cacheDelRes['message'] == "success":
    #         print("*******************系统盘列表删除成功**************************")
    #     else:
    #         print("*******************缓存盘列表删除失败,接口返回结果为：{}".format(cacheDelRes))

'''创建快照'''
def creCloudDiskSnapshot(volumeId):
    headers = {
        "Content-Type": "application/json",
        "Authorization": Token
    }

    reqUrl = urlConfigs.dataDiskSnapshot
    print(reqUrl)
    reqParam = {
    "name":"snapShot_"+str(random.randint(1,100)),
    "description":"create snapshot for datadisk",
    "volume": volumeId
}
    print("数据盘创建快照的请求参数是：{}".format(reqParam))
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.post(url=reqUrl, headers=headers, json=reqParam,verify=False).json()
    print("数据盘创建快照的响应结果是: {}".format(result))


'''卸载数据盘'''
def datachDataCloudDisk():

    headers ={
        "Content-Type":"application/json",
        "Authorization": Token
    }
    reqUrl = urlConfigs.cloudDisk
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers,verify=False).json()
    # print("响应结果是:\n {}".format(result))
    if result['message']=='success':
        data = result['data']
        data_disks = data['data_disks']
        if len(data_disks) > 0:
            for i in range(len(data_disks)):
                diskId = data_disks[i]['id']
                diskStatus = data_disks[i]['status']
                '''如果是加载状态的云硬盘，获取加载信息'''
                if diskStatus == 'in-use':
                    attachInfoUrl = urlConfigs.attachCDInfo + diskId + '/'
                    attachInfoResult = requests.get(url=attachInfoUrl, headers=headers, verify=False).json()
                    if attachInfoResult['message']=='success':
                        '''获取加载server的id信息'''
                        attachServerId = attachInfoResult['data'][0]['attachments'][0]['server_id']
                        '''对已加载的云硬盘进行卸载'''
                        detachCloudDiskUrl = urlConfigs.cloudDisk + diskId + '/detachments/'
                        datachParam = {
                            "server_id": attachServerId
                        }
                        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                        detachResult = requests.post(url=detachCloudDiskUrl, headers=headers, json=datachParam,verify=False).json()
                        if detachResult['message']=='success':
                            print("*******************卸载云硬盘{}成功**************************".format(diskId))
                        else:
                            print("*******************卸载云硬盘失败，响应结果为：{}".format(detachResult))

                    else:
                        print("*******************获取云硬盘加载信息失败，响应结果为: {}".format(attachInfoResult))














# createCloudDisk("1","76edcd32140e47bca8c182b4d3d6c90a", "LeonaTestPool")
# batchCreateCloudDisk(5,1,"76edcd32140e47bca8c182b4d3d6c90a", "LeonaTestPool")
# getCloudDiskList()
# delCloudDisk()
# creCloudDiskSnapshot("eff1759c-dde9-4508-93e7-b8cb57bf470e")
# datachDataCloudDisk()

