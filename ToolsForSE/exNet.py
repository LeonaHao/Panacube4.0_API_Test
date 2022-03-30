# -*- coding: utf-8 -*-
# @Time: 2022/3/18 18:37
# @Author: Leona
# @File: exNet.py

import requests
import urllib3
from configs.urlConfigs import subnetUrl
from lib.PanaCubeCommon import login



Token = login()

'''获取外部网络子网列表'''
def getSubnetList(exNetId):

    try:
        headers ={
            "Content-Type":"application/json",
            "Authorization": Token,
        }
        reqUrl = subnetUrl + '?network_id=' + str(exNetId)
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result = requests.get(url=reqUrl, headers=headers,verify=False).json()
        # print("响应结果是:  {}".format(result))
        data = result['data']
        dataDiskList = []
        if len(data) > 0:
            print("共有{}个子网".format(len(data)))
            for i in range(len(data)):
                dataDiskList.extend([data[i]['id']])
        else:
            print("数据盘列表为空")

        # print("获取的子网列表信息为：{}".format(dataDiskList))
        return dataDiskList

    except Exception as e:
        print(e)


'''删除外部网络子网'''
def delExnetSub(exNetId):
    headers ={
        "Content-Type":"application/json",
        "Authorization": Token
    }
    reqUrl = subnetUrl + '/'
    reqParam ={}
    exSubList = getSubnetList(exNetId)
    # time.sleep(30)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    for subnetId in exSubList:
        result = requests.delete(url=reqUrl + str(subnetId), headers=headers,json=reqParam,verify=False).json()
        if result['message'] == "success":
            print("*******************外部网络子网删除成功**************************")
        else:
            print("*******************外部网络子网删除失败:{}**************************".format(result))










# getSubnetList("e8acbd43-1619-4be6-b27e-cebada45ae40")
delExnetSub("e8acbd43-1619-4be6-b27e-cebada45ae40")