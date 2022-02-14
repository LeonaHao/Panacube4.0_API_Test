# coding = utf-8
# @author = Leona

import random

'''
封装PanaCube的常用方法
'''
import requests
import urllib3
from configs import urlConfigs
from lib import MySQLHelper

#获取登录token
def login():
    try:
        headers = {"Content-Type":"application/json"}
        reqUrl = urlConfigs.loginUrl
        reqParam = {
            "username":"admin",
            "password":"P@ssw0rd"    #P@ssw0rd，  Aa12345678
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result = requests.post(url=reqUrl, headers=headers,json=reqParam,verify=False).json()
        token = result['data']['token']
        Token = 'TOKEN ' + str(token)
        return Token
    except Exception as e:
        print(e)



def getSysDiskInfo():
    try:
        Token = login()
        headers = {"Content-Type":"application/json",
                   "Authorization":Token}
        reqUrl = urlConfigs.cloudDisk +'?page=1&size=10&info=sys'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result = requests.get(url=reqUrl, headers=headers,verify=False).json()
        if len(result['data'])!=0:
            sysDiskInfo = result['data'][0]
            # print(sysDiskInfo)
            sysDiskId = sysDiskInfo['id']
            sysDiskName = sysDiskInfo['name']
            sysDisksize = sysDiskInfo['size']
            sysDisktype = sysDiskInfo['disk_type']
            sysDiskStatus = sysDiskInfo['disk_status']
            sysDiskDes = sysDiskInfo['description']
            sysDiskCreTime = sysDiskInfo['created_time']
            sysDiskSnap = sysDiskInfo['is_snapshoted']
            projectName = sysDiskInfo['project_name']
            projectId = sysDiskInfo['project_id']
            poolName = sysDiskInfo['pool_name']
            return sysDiskId,sysDiskName,sysDisksize,sysDisktype,sysDiskStatus,sysDiskDes,sysDiskCreTime,sysDiskSnap,projectName,projectId,poolName
        else:
            pass
    except Exception as e:
        print(e)



def getDataDiskInfo():
    try:
        Token = login()
        headers = {"Content-Type":"application/json",
                   "Authorization":Token}
        reqUrl = urlConfigs.cloudDisk +'?page=1&size=10&info=data'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result = requests.get(url=reqUrl, headers=headers,verify=False).json()
        print(result)
        if len(result['data'])!=0:
            dataDiskInfo = result['data'][0]
            # print(dataDiskInfo)
            dataDiskId = dataDiskInfo['id']
            dataDiskName = dataDiskInfo['name']
            dataDisksize = dataDiskInfo['size']
            dataDisktype = dataDiskInfo['disk_type']
            dataDiskStatus = dataDiskInfo['disk_status']
            dataDiskDes = dataDiskInfo['description']
            dataDiskShareVol = dataDiskInfo['share_vol']
            dataDiskCreTime = dataDiskInfo['created_time']
            dataDiskSnap = dataDiskInfo['is_snapshoted']
            dataDiskAttachInstance = dataDiskInfo['instances']
            dataDiskAttachPath = dataDiskInfo['path']
            projectName = dataDiskInfo['project_name']
            projectId = dataDiskInfo['project_id']
            poolName = dataDiskInfo['pool_name']
            return dataDiskId,dataDiskName,dataDisksize,dataDisktype,dataDiskStatus,dataDiskDes,dataDiskShareVol,dataDiskCreTime,dataDiskSnap,dataDiskAttachInstance,dataDiskAttachPath,projectName,projectId,poolName
        else:
            pass
    except Exception as e:
        print(e)



def paramCombine(**kwargs):
    a = ""
    # x是key值，y是value值, 通过循环，拼接参数
    for x, y in kwargs.items():
        a += "%s=%s" % (x, y) + "&"
    # return时要剔除最后的&符号
    return a[0:len(a) - 1]



def getShareService():
    try:
        Token = login()
        headers = {"Content-Type":"application/json",
                   "Authorization":Token}
        reqUrl = urlConfigs.serviceUrl
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result = requests.get(url=reqUrl, headers=headers,verify=False).json()
        print(result['data'])
        return result['data']


    except Exception as e:
        print(e)



getShareService()










