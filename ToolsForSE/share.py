#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Leona
# @time: 2020-06-16

import requests
import urllib3
from configs import urlConfigs
from lib.PanaCubeCommon import login
from random import randint



Token = login()

'''创建共享'''
def createShare(num, projectId, projectName,type):

    headers ={
        "Content-Type":"application/json",
        "Authorization": Token
    }
    reqUrl = urlConfigs.shareUrl
    if type == 'cn':
        reqParam = {
                    "name":"cAndNshare"+str(num),
                    "cifs":"yes",
                    "nfs":"yes",
                    "s3":"no",
                    "browseable":"yes",
                    "read_only":"no",
                    "create_mask":"0744",
                    "directory_mask":"0755",
                    "guest_ok":"yes",
                    "sync":"no",
                    "no_root_squash":"yes",
                    "auth_enable":"disable",
                    "compression":"off",
                    "dedup":"off",
                    "volblocksize":"8K",
                    "share_type":0,
                    "agree_type":[
                        "CIFS",
                        "NFS"
                    ],
                    "project_id":projectId,
                    "project_name":projectName
                }
    elif type == 'c':
        reqParam ={
                "name":"cShare" + str(num),
                "cifs":"yes",
                "nfs":"no",
                "s3":"no",
                "browseable":"yes",
                "read_only":"no",
                "create_mask":"0744",
                "directory_mask":"0755",
                "guest_ok":"yes",
                "sync":"no",
                "no_root_squash":"no",
                "auth_enable":"disable",
                "compression":"off",
                "dedup":"off",
                "volblocksize":"8K",
                "share_type":0,
                "agree_type":[
                    "CIFS"
                ],
                "project_id":projectId,
                "project_name":projectName
            }
    elif type == 'n':
        reqParam ={
                "name":"nShare"+str(num),
                "cifs":"no",
                "nfs":"yes",
                "s3":"no",
                "browseable":"yes",
                "read_only":"no",
                "create_mask":"0744",
                "directory_mask":"0755",
                "guest_ok":"no",
                "sync":"no",
                "no_root_squash":"yes",
                "auth_enable":"disable",
                "compression":"off",
                "dedup":"off",
                "volblocksize":"8K",
                "share_type":0,
                "agree_type":[
                    "NFS"
                ],
                "project_id":projectId,
                "project_name":projectName
            }
    elif type == 's':
        reqParam = {
                "name":"s" + str(num),
                "cifs":"no",
                "nfs":"no",
                "s3":"yes",
                "browseable":"yes",
                "read_only":"no",
                "create_mask":"0744",
                "directory_mask":"0755",
                "guest_ok":"no",
                "sync":"no",
                "no_root_squash":"no",
                "auth_enable":"disable",
                "port": str(randint(9000,10000)),
                "access_key":"123456",
                "secret_key":"12345678",
                "compression":"off",
                "dedup":"off",
                "volblocksize":"8K",
                "share_type":2,
                "agree_type":[
                    "S3"
                ],
                "project_id":projectId,
                "project_name":projectName
            }
    else:
        print("参数类型错误，请退出重填！")


    print("请求参数是:  {}".format(reqParam))
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.post(url=reqUrl, headers=headers,json=reqParam,verify=False).json()
    print("响应结果是:  {}".format(result))
    if result['message']=='success':
        print("*******************成功创建共享**************************")
    else:
        print("*******************创建共享失败，响应结果为：{}".format(result))

'''批量共享'''
def batchCreateShare(n, num,projectId, projectName,type):
    for i in range(n):
        createShare(num,projectId, projectName,type)
        num = num + 1

'''获取共享列表'''
def getShareList(projectId,projectName):
    headers ={
        "Content-Type":"application/json",
        "Authorization": Token,
        "PROJECT-ID": projectId,
        "PROJECT-NAME": projectName

    }
    reqUrl = urlConfigs.shareUrl
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers,verify=False).json()
    # print("响应结果是:\n {}".format(result))
    if result['message']=='success':
        data = result['data']
        shareIdList = []

        if len(data) > 0:
            for i in range(len(data)):
                shareId = data[i]['id']
                shareIdList.append(shareId)

        print("获取的共享列表信息为：{}".format(shareIdList))
        return shareIdList

    else:
        print("*******************获取共享列表信息失败，响应结果为：{}".format(result))

'''删除共享列表'''
def delShare(projectId,projectName):
    headers ={
        "Content-Type":"application/json",
        "Authorization": Token,
        "PROJECT-ID": projectId,
        "PROJECT-NAME": projectName
    }

    shareIdList = getShareList(projectId,projectName)
    if len(shareIdList) > 0:
        reqUrl = urlConfigs.shareDelUrl
        reqParam = {
            "ids": shareIdList
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        shareDelRes = requests.delete(headers=headers,url=reqUrl,json=reqParam,verify=False).json()
        # print(shareDelRes)
        if shareDelRes['message'] == "success":
            print("*******************共享列表删除成功**************************")
        else:
            print("*******************共享列表删除失败,接口返回结果为：{}".format(shareDelRes))
    else:
        print("*******************共享列表为空，无需删除**************************")





# createShare(2,"1732f00b451a48eb8ee65a7362dbb5dc","默认池","s")
# batchCreateShare(3,3,"1732f00b451a48eb8ee65a7362dbb5dc","默认池","n")
# getShareList("1732f00b451a48eb8ee65a7362dbb5dc","%E9%BB%98%E8%AE%A4%E6%B1%A0")
# delShare("1732f00b451a48eb8ee65a7362dbb5dc","%E9%BB%98%E8%AE%A4%E6%B1%A0")
