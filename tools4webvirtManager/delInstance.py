# -*- coding: utf-8 -*-
# @Time: 2022/4/25 19:08
# @Author: Leona
# @File: delInstance.py

import requests
import time

cookie = "sessionid=hxy7b058zvm61cp48z8ztci4e3y2lnbg; csrftoken=bHm3vUNP87HP1IQr8zqQ4XTKeKFVc573; token=4-b8ddff25-0407-7cf1-84c0-1a5e5d18b7a4"
getInstanceUrl= 'http://192.168.3.171:8007/info/insts_status/4/'
delInstanceUrl = 'http://192.168.3.171:8007/instance/4/'


def getInstanceNameList():
    headers = {"Content-Type":"application/x-www-form-urlencoded",
               "Cookie":cookie}
    url= getInstanceUrl
    instanceNameList = []
    res = requests.get(headers=headers,url=url,verify=False).json()

    for item in res:
        instanceNameList.append(item['name'])
    print(instanceNameList)
    return instanceNameList

def delInstanceList():
    headers = {"Content-Type":"application/x-www-form-urlencoded",
               "Cookie":cookie}
    instanceNameList = getInstanceNameList()

    for VMname in instanceNameList:
        url= delInstanceUrl + str(VMname) + '/'
        print(url)
        formData ={"csrfmiddlewaretoken":cookie.split(";")[1].split("=")[1],
                   "delete_disk": True,
                   "delete":''
                   }
        print('请求参数为：{}'.format(formData))
        res = requests.post(headers=headers,url=url, data=formData,verify=False)
        print(res.status_code)
        print("***********删除虚拟机{}成功**************".format(str(VMname)))
        time.sleep(5)


def forceDelInstance():



delInstanceList()


