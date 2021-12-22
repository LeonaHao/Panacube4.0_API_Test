# -*- coding: utf-8 -*-
# @Time: 2021/12/14 16:02
# @Author: Leona
# @File: instanceCreate.py

import requests
import random
import time
from lib.PanaCubeCommon import login
from configs.urlConfigs import networktUrl,imageUrl,instanceUrl


def creInstance(projectId, projectName):
    token = login()
    headers = {"Content-Type":"application/json",
               "Authorization": token,
               "PROJECT-ID": projectId,
               "PROJECT-NAME": projectName
               }

    '''获取网络信息'''
    networkInfo = requests.get(url=networktUrl, headers=headers,verify=False).json()
    if len(networkInfo['data']) > 0:
        netId = networkInfo['data'][0]['id']
        subnetId = networkInfo['data'][0]['subnets'][0]['id']
    else:
        pass

    '''获取镜像信息'''
    imageInfo = requests.get(url=imageUrl, headers=headers,verify=False).json()
    if len(imageInfo['data']) > 0:
        imageId = imageInfo['data'][0]['id']

    '''创建组件'''
    reqParam ={
        "name":"LC_"+  str(random.randint(1,1000)),
        "project":projectName,
        "location":"node-3",
        "passwd":"",
        "cpu":1,
        "memory":1024,
        "network":{
            "net_id":netId,
            "fixed_ips":[
                {
                    "subnet_id":subnetId
                }
            ]
        },
        "disk":[
            {
                "name":"AD2",
                "size":2,
                "path":"/mnt/AD2_"+ str(random.randint(1,1000))
            },
            {
                "name":"AD1",
                "size":1,
                "path":"/mnt/AD1_"+ str(random.randint(1,1000))
            }
        ],
        "storage":{
            "storage_pool":projectId,
            "size":"1"
        },
        "source":{
            "type":"image",
            "fingerprint":imageId
        },
        "hostname":"",
        "security_group_id":"",
        "project_id":projectId,
        "project_name":projectName
    }
    instanceInfo = requests.post(url=instanceUrl, headers=headers,json=reqParam,verify=False).json()
    #等待1分钟，确保组件创建完成
    time.sleep(30)
    if instanceInfo['code'] == 0:
        print("************************云组件创建成功*****************************")
    else:
        print("************************云组件创建失败*****************************")



if __name__ == '__main__':
    creInstance('3adfec2c1f044e98a41e6c3649651dc8','LeonaTestPool1220')
