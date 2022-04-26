# -*- coding: utf-8 -*-
# @Time: 2022/4/16 11:08
# @Author: Leona
# @File: creInstance.py

import requests
import time

cookie = "sessionid=hxy7b058zvm61cp48z8ztci4e3y2lnbg; csrftoken=bHm3vUNP87HP1IQr8zqQ4XTKeKFVc573; token=4-b8ddff25-0407-7cf1-84c0-1a5e5d18b7a4"
reqUrl= 'http://192.168.3.171:8007/create/2/'
image = "kylin10Mirror_"

def creInstance(Num):
    headers = {"Content-Type":"application/x-www-form-urlencoded",
               "Cookie":cookie}

    url= reqUrl

    formData ={"csrfmiddlewaretoken":cookie.split(";")[1].split("=")[1],
               "name":"VM" + str(Num),
               "vcpu":1,
               "host_model":True,
               "memory":1024,
               "images": image +str(Num) + ".qcow2",
               "image-control": image + str(Num) + ".qcow2",
               "cache_mode": "default",
               "networks": "default",
               "network-control": "default",
               "virtio": True,
               "create": 1
               }
    print('请求参数为：{}'.format(formData))
    res = requests.post(headers=headers,url=url, data=formData,verify=False)
    print(res.status_code)
    print("***********创建第{}个虚拟机成功**************".format(str(Num)))



def batchCreInstance(startNum, EndNum):
    for i in range(startNum,EndNum):
        creInstance(i)
        time.sleep(5)


batchCreInstance(41,58)



# creInstance(5)

