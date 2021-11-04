# coding = utf-8
# @author = Leona

import random

'''
封装PanaCube的常用方法
'''
import requests
import urllib3
from configs import urlConfigs

#获取登录token
def login():
    try:
        headers = {"Content-Type":"application/json"}
        reqUrl = urlConfigs.loginUrl
        reqParam = {
            "username":"admin",
            "password":"Aa12345678"    #P@ssw0rd
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result = requests.post(url=reqUrl, headers=headers,json=reqParam,verify=False).json()
        token = result['data']['token']
        Token = 'TOKEN ' + str(token)
        return Token
    except Exception as e:
        print(e)





def paramCombine(**kwargs):
    a = ""
    # x是key值，y是value值, 通过循环，拼接参数
    for x, y in kwargs.items():
        a += "%s=%s" % (x, y) + "&"
    # return时要剔除最后的&符号
    return a[0:len(a) - 1]






