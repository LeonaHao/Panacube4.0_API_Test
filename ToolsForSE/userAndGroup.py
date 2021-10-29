#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Leona
# @time: 2020-06-17

import requests
import urllib3
from configs import urlConfigs
from lib.PanaCubeCommon import login,  getProjectInfo


'''创建用户--------------待完成'''
def createUser(poolId,num):
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
    reqUrl = urlConfigs.userUrl
    reqParam = {
        "name": "user"+ str(num),
        "password": "11111111",
        "group": []
    }
    print("请求参数是:  {}".format(reqParam))
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.post(url=reqUrl, headers=headers,json=reqParam,verify=False).json()
    print("响应结果是:  {}".format(result))
    if result['message']=='success':
        print("*******************成功创建共享用户**************************")
    else:
        print("*******************创建共享用户失败，响应结果为：{}".format(result))

'''批量创建用户'''
def batchCreateUser(n, poolId,num):
    for i in range(n):
        createUser(poolId,num)
        num = num + 1

'''创建用户组--------------待完成'''
def createUserGroup(poolId,num):
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
    reqUrl = urlConfigs.userGroupUrl
    reqParam = {
        "name":"userGroup" + str(num),
    }
    print("请求参数是:  {}".format(reqParam))
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.post(url=reqUrl, headers=headers,json=reqParam,verify=False).json()
    print("响应结果是:  {}".format(result))
    if result['message']=='success':
        print("*******************成功创建用户组**************************")
    else:
        print("*******************创建用户组失败，响应结果为：{}".format(result))

'''批量创建用户组'''
def batchCreateUserGroup(n, poolId,num):
    for i in range(n):
        createUserGroup(poolId,num)
        num = num + 1

'''获取用户列表'''
def getUserList():
    # projectInfo = getProjectInfo()
    # projectId = projectInfo[int(poolId)][0]
    # projectName = projectInfo[int(poolId)][1]

    headers ={
        "Content-Type":"application/json",
        "Authorization": login()
        # "POOL-ID": poolId,
        # "PROJECT-ID": projectId,
        # "PROJECT-NAME": projectName

    }
    reqUrl = urlConfigs.userUrl
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers,verify=False).json()
    # print("响应结果是:\n {}".format(result))
    if result['message']=='success':
        data = result['data']
        userList = []

        if len(data) > 0:
            for i in range(len(data)):
                userName = data[i]['name']
                userList.append(userName)

        print("获取的共享用户列表信息为：{}".format(userList))
        return userList

    else:
        print("*******************获取共享用户列表信息失败，响应结果为：{}".format(result))

'''删除用户列表'''
def delUser():
    # projectInfo = getProjectInfo()
    # projectId = projectInfo[int(poolId)][0]
    # projectName = projectInfo[int(poolId)][1]

    headers ={
        "Content-Type":"application/json",
        "Authorization": login()
        # "POOL-ID": poolId,
        # "PROJECT-ID": projectId,
        # "PROJECT-NAME": projectName
    }

    userList = getUserList()

    if len(userList) > 0:
        reqUrl = urlConfigs.userDelUrl
        reqParam = {
            "names": userList
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        userDelRes = requests.post(headers=headers,url=reqUrl,json=reqParam,verify=False).json()
        print(userDelRes)
        if userDelRes['message'] == "success":
            print("*******************共享用户列表删除成功**************************")
        else:
            print("*******************共享用户列表删除失败,接口返回结果为：{}".format(userDelRes))


'''获取用户组列表'''
def getUserGroupList():
    # projectInfo = getProjectInfo()
    # projectId = projectInfo[int(poolId)][0]
    # projectName = projectInfo[int(poolId)][1]

    headers ={
        "Content-Type":"application/json",
        "Authorization": login()
        # "POOL-ID": poolId,
        # "PROJECT-ID": projectId,
        # "PROJECT-NAME": projectName

    }
    reqUrl = urlConfigs.userGroupUrl
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers,verify=False).json()
    # print("响应结果是:\n {}".format(result))
    if result['message']=='success':
        data = result['data']
        userGroupList = []

        if len(data) > 0:
            for i in range(len(data)):
                userGroup = data[i]['name']
                userGroupList.append(userGroup)

        print("获取的共享用户组列表信息为：{}".format(userGroupList))
        return userGroupList

    else:
        print("*******************获取共享用户组列表信息失败，响应结果为：{}".format(result))


'''删除用户组列表'''
def delUserGroup():
    # projectInfo = getProjectInfo()
    # projectId = projectInfo[int(poolId)][0]
    # projectName = projectInfo[int(poolId)][1]

    headers ={
        "Content-Type":"application/json",
        "Authorization": login()
        # "POOL-ID": poolId,
        # "PROJECT-ID": projectId,
        # "PROJECT-NAME": projectName
    }

    userGroupList = getUserGroupList()

    if len(userGroupList) > 0:
        reqUrl = urlConfigs.userGroupDelUrl
        reqParam = {
            "names": userGroupList
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        userGroupDelRes = requests.post(headers=headers,url=reqUrl,json=reqParam,verify=False).json()
        print(userGroupDelRes)
        if userGroupDelRes['message'] == "success":
            print("*******************共享用户组列表删除成功**************************")
        else:
            print("*******************共享用户组列表删除失败,接口返回结果为：{}".format(userGroupDelRes))


# createUser("40",2)
# batchCreateUser(10,"676",1)
# createUserGroup("40",1)
# batchCreateUserGroup(10,"676",1)
# getUserList()
delUser()
# getUserGroupList("5")
delUserGroup()