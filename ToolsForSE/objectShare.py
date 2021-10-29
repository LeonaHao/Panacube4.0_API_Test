#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Leona
# @time: 2020-06-17

import requests
import urllib3
from configs import urlConfigs
from lib.PanaCubeCommon import login,  getProjectInfo



'''创建对象共享'''
def createObjShare(poolId,num):
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
    reqUrl = urlConfigs.objShareUrl
    reqParam = {
        "name":"objshare" + str(num),
    }
    print("请求参数是:  {}".format(reqParam))
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.post(url=reqUrl, headers=headers,json=reqParam,verify=False).json()
    print("响应结果是:  {}".format(result))
    if result['message']=='success':
        print("*******************成功创建对象共享**************************")
    else:
        print("*******************创建对象共享失败，响应结果为：{}".format(result))

'''批量创建对象共享'''
def batchCreateObjShare(n, poolId,num):
    for i in range(n):
        createObjShare(poolId,num)
        num = num + 1

'''获取对象共享列表'''
def getObjShareList(poolId):
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
    reqUrl = urlConfigs.objShareUrl
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers,verify=False).json()
    # print("响应结果是:\n {}".format(result))
    if result['message']=='success':
        data = result['data']
        objShareList = []

        if len(data) > 0:
            for i in range(len(data)):
                ojbShareName = data[i]['name']
                objShareList.append(ojbShareName)

        print("获取的对象共享列表信息为：{}".format(objShareList))
        return objShareList

    else:
        print("*******************获取对象共享列表信息失败，响应结果为：{}".format(result))

'''删除对象共享列表'''
def delObjShare(poolId):
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

    ojbShareList = getObjShareList(poolId)

    if len(ojbShareList) > 0:
        reqUrl = urlConfigs.objShareDelUrl
        reqParam = {
            "buckets": ojbShareList
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        objShareDelRes = requests.post(headers=headers,url=reqUrl,json=reqParam,verify=False).json()
        # print(objShareDelRes)
        if objShareDelRes['message'] == "success":
            print("*******************对象共享列表删除成功**************************")
        else:
            print("*******************对象共享列表删除失败,接口返回结果为：{}".format(objShareDelRes))
    else:
        pass


# createObjShare("40",2)
# batchCreateObjShare(10,"676",1)
# getObjShareList("5")
# delObjShare("741")