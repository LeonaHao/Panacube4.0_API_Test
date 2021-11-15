# coding = utf-8
# @author = Leona

import random
import time

'''
筋斗云》智能存储》快照   相关操作
'''
import requests
import urllib3
import random
from configs import urlConfigs
from lib.PanaCubeCommon import login

Token = login()

'''获取业务池信息,返回业务池的id和名称'''
def getPoolInfo(projectId):
    reqUrl = urlConfigs.cloudPoolListUrl + '/'+ str(projectId)
    headers ={
        "Content-Type":"application/json",
        "Authorization": Token
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers,verify=False).json()
    # print("响应结果为： {}".format(result))
    return result['data']['id'],result['data']['name']


'''创建业务池快照'''
def createPoolSnapshot(projectId):
    reqUrl = urlConfigs.poolSnap
    headers ={
        "Content-Type":"application/json",
        "Authorization": Token
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    projectName = getPoolInfo(projectId)
    reqParam = {
        "name":"poolSnapshot4" + str(projectName[1]) + str(random.randint(0,1000)),
        "project_id":projectId
    }
    print("请求参数是:  {}".format(reqParam))
    result = requests.post(url=reqUrl, headers=headers,json=reqParam, verify=False).json()
    print("响应结果是:  {}".format(result))
    if result['message']=='success':
        print("*******************创建业务池快照成功**************************")
    else:
        print("*******************创建业务池快照失败**************************")

'''批量创建业务池快照'''
def batchCreatePoolSnapshot(n, projectId):
    for i in range(n):
        createPoolSnapshot(projectId)


'''获取业务池快照列表'''
def getPoolSnapList():
    headers ={
        "Content-Type":"application/json",
        "Authorization": Token
    }
    reqUrl = urlConfigs.poolSnap
    # print(reqUrl)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers,verify=False).json()
    # print("响应结果是:\n {}".format(result))
    data=result['data']
    if result['message']=='success':
        idList = []
        # pathList = []
        for i in range(len(data)):
            id = data[i]['id']
            idList.append(id)
            # path = data[i]['path']
            # pathList.append(path)
        # print("*******************获取卷guild如下所示**************************")
        print("获取业务池快照列表的信息为：{}".format(idList))
        return idList
    else:
        print("*******************获取业务池快照列表**************************")


'''删除业务池快照'''
def delPoolSnap():
    poolSnapList = getPoolSnapList()
    time.sleep(30)
    headers ={
        "Content-Type":"application/json",
        "Authorization": Token
    }
    reqUrl = urlConfigs.delPoolSnap
    reqParam ={
            "ids":poolSnapList
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.delete(url=reqUrl, headers=headers,json=reqParam,verify=False).json()
    if result['message'] == "success":
        print("*******************业务池快照删除成功**************************")
    else:
        print("*******************业务池快照删除失败:{}**************************".format(result))



'''获取云组件快照列表'''
def getInstanceSnapshotList():
    headers ={
        "Content-Type":"application/json",
        "Authorization": Token
    }
    reqUrl = urlConfigs.instanceSnap
    print (reqUrl)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers,verify=False).json()
    print(result)
    data=result['data']
    if result['message']=='success':
        instanceSnapList = {}
        for i in range(len(data)):
            instanceId = data[i]['instance_id']
            instanceSnapList[instanceId] =(data[i]['snapshot_name'],data[i]['project_id'])

        print("获取云组件快照列表信息为：{}".format(instanceSnapList))
        return instanceSnapList
    else:
        print("*******************获取云组件快照列表失败**************************")



'''获取云硬盘快照列表'''
def getDiskSnapshotList():
    headers ={
        "Content-Type":"application/json",
        "Authorization": Token
    }
    reqUrl = urlConfigs.diskSnap
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.get(url=reqUrl, headers=headers,verify=False).json()

    data=result['data']
    if result['message']=='success':
        diskSnapList = []
        for i in range(len(data)):
            diskSnapId = data[i]['snapshot_id']
            diskSnapList.append(diskSnapId)

        print("获取云硬盘快照列表信息为：{}".format(diskSnapList))
        return diskSnapList
    else:
        print("*******************获取云硬盘快照列表失败**************************")





'''删除云组件快照'''
def delInstanceSnap():
    instanceSnapList = getInstanceSnapshotList()
    # time.sleep(30)

    for instanceId, instanceInfo in instanceSnapList.items():
        headers = {
            "Content-Type": "application/json",
            "Authorization": Token,
            "PROJECT-ID":instanceInfo[1]
        }
        reqUrl = urlConfigs.delInstanceSnap + str(instanceId) + '/snapshots/' + str(instanceInfo[0])
        # reqParam = {}
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result = requests.delete(url=reqUrl, headers=headers,verify=False).json()
        time.sleep(2)
        if result['message'] == "success":
            print("*******************云组件快照{}删除成功**************************".format(str(instanceInfo[0])))
        else:
            print("*******************云组件快照{}删除失败**************************".format(str(instanceInfo[0])))


'''删除云硬盘快照'''
def delDiskSnap():
    diskSnapList = getDiskSnapshotList()
    # time.sleep(30)
    headers ={
        "Content-Type":"application/json",
        "Authorization": Token
    }
    reqUrl = urlConfigs.delDiskSnap
    reqParam ={
            "ids":diskSnapList
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    result = requests.post(url=reqUrl, headers=headers,json=reqParam,verify=False).json()
    if result['message'] == "success":
        print("*******************云硬盘快照删除成功**************************")
    else:
        print("*******************云硬盘快照删除失败:{}**************************".format(result))




# createPoolSnapshot("76edcd32140e47bca8c182b4d3d6c90a")
batchCreatePoolSnapshot(2,"76edcd32140e47bca8c182b4d3d6c90a")
# getPoolSnapList()
# delPoolSnap()
# createVolume("225", 1)
# batchCreateVolume(5,"228",1)

# getInstanceSnapshotList()
# getDiskSnapshotList()
# delPoolSnap()
# delInstanceSnap()
# delDiskSnap()
# getVolumePathList("40")
# createVolumeSnapShot("228")
# getVolumeSnapshotList("5")
# delVolumeSnapshot("23")


