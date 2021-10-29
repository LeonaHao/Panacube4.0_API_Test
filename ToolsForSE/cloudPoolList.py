# coding = utf-8
# @author = Leona

#响应结果一直报 **********响应结果为：{'code': 1005, 'message': '缺少认证信息', 'data': None, 'level': 1}，登录获取的token有问题


import requests
from configs import urlConfigs
from lib.PanaCubeCommon import commonHeader, login

Token = login()

def getCloudPoolList():
    headers = {'Content-Type': 'application/json', 'Authorization': Token}
    reqUrl = urlConfigs.cloudPoolListUrl
    result = requests.get(url=reqUrl, headers=headers).json()
    print("**********响应结果为："+str(result))


if __name__ == '__main__':
    getCloudPoolList()
