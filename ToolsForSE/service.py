#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Leona
# @time: 2020-06-16

import requests
import urllib3
from configs import urlConfigs
from lib.PanaCubeCommon import login,  getProjectInfo

'''获取服务列表并开启服务'''
def getAndEnableService(poolId):
    projectInfo = getProjectInfo()
    projectId = projectInfo[int(poolId)][0]
    projectName = projectInfo[int(poolId)][1]

    headers = {
        "Content-Type": "application/json",
        "Authorization": login(),
        "POOL-ID": poolId,
        "PROJECT-ID": projectId,
        "PROJECT-NAME": projectName

    }
    reqUrl = urlConfigs.serviceUrl
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers, verify=False).json()
    data = result['data']
    if result['message']=='success':
        for i in range(len(data)):
            serviceName = data[i]['name']
            serviceStatus = data[i]['status']
            print("*******************{}的服务状态为：{}".format(serviceName,serviceStatus))
            '''如果服务是停止的，则开启服务'''
            if serviceStatus == False:
                startServiceUrl = urlConfigs.startServiceUrl
                startServiceParam = {
                    "services":[
                                serviceName.lower()
                        ]
                    }
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                result = requests.post(url=startServiceUrl, headers=headers,json=startServiceParam,verify=False).json()
                if result['message']=='success':
                    print("*******************{}服务开启成功！".format(serviceName))
                else:
                    print("*******************服务开启失败，响应结果为：{}".format(result))

    else:
        print("*******************获取服务列表失败，响应结果为：{}".format(result))

'''获取服务列表并停止服务'''
def getAndDisableService(poolId):
    projectInfo = getProjectInfo()
    projectId = projectInfo[int(poolId)][0]
    projectName = projectInfo[int(poolId)][1]

    headers = {
        "Content-Type": "application/json",
        "Authorization": login(),
        "POOL-ID": poolId,
        "PROJECT-ID": projectId,
        "PROJECT-NAME": projectName

    }
    reqUrl = urlConfigs.serviceUrl
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers, verify=False).json()
    data = result['data']
    if result['message']=='success':
        for i in range(len(data)):
            serviceName = data[i]['name']
            serviceStatus = data[i]['status']
            print("*******************{}的服务状态为：{}".format(serviceName,serviceStatus))
            '''如果服务是开启的，则停止服务'''
            if serviceStatus == True:
                stopServiceUrl = urlConfigs.stopServiceUrl
                stopServiceParam = {
                    "services":[
                                serviceName.lower()
                        ]
                    }
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                result = requests.post(url=stopServiceUrl, headers=headers,json=stopServiceParam,verify=False).json()
                if result['message']=='success':
                    print("*******************{}服务关闭成功！".format(serviceName))
                else:
                    print("*******************服务关闭失败，响应结果为：{}".format(result))

    else:
        print("*******************获取服务列表失败，响应结果为：{}".format(result))

# getAndEnableService("40")
# getAndDisableService("5")