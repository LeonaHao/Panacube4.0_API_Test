# -*- coding: utf-8 -*-
# @Time: 2021/12/22 17:04
# @Author: Leona
# @File: restoreInstanceSnapshot.py


# -*- coding: utf-8 -*-
# @Time: 2021/12/22 17:01
# @Author: Leona
# @File: restoreInstanceSnap.pyd.py

import unittest
import requests
import json
import time
from configs.urlConfigs import instanceUrl, logoutUrl
from lib.PanaCubeCommon import login
from toolsForSE.instanceCreate import creInstance
from lib.PanacubeCommonQuery import getLatestInstance,getLatestInstanceSnap
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
智能存储》快照管理》回滚云组件快照
"""


class restoreInstanceSnap(unittest.TestCase):
    """智能存储》快照管理》回滚云组件快照"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token, projectId, projectName
        token = login()
        projectId="577d21c9411744a4b619c8966f69ec18"
        projectName="LeonaTestPool1213"

        "创建1个云组件"
        creInstance(projectId,projectName)
        time.sleep(5)

        '''获取最新的云组件信息'''
        global getLatestInstanceInfo
        getLatestInstanceInfo = getLatestInstance(projectId)

        '''获取云组件磁盘信息'''
        headers ={"Content-Type":"application/json", "Authorization":token, "PROJECT-ID":projectId, "PROJECT-NAME":projectName}
        volumeUrl = instanceUrl + '/' + str(getLatestInstanceInfo['id']) + '/volumes?volume_type=0'
        volumeRes = requests.get(url=volumeUrl,headers=headers,verify=False ).json()
        global volumeIds
        volumeIds = []
        for volume in volumeRes['data']:
            volumeIds.append(volume['volume_id'])

        "创建1个云组件快照"
        volumeSnapParam ={
            "snapshot_name":"snap4" + getLatestInstanceInfo['name'],
            "volumes_ids":volumeIds,
            "project_id":projectId,
            "project_name":projectName
        }
        creInsUrl =instanceUrl+'/'+str(getLatestInstanceInfo['id'])+'/snapshots'
        instanceSnapRes = requests.post(url=creInsUrl,headers=headers,json=volumeSnapParam,verify=False).json()
        time.sleep(30)

        '''获取最新的云组件快照信息'''
        global instanceSnapInfo
        instanceSnapInfo = getLatestInstanceSnap(projectId)


    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************回滚云组件快照接口开始****************")
        headers2 ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqUrl2 = instanceUrl + '/'+str(instanceSnapInfo['server_id'])
        print("*"*80)
        print(reqUrl2)
        print("*"*80)

        '''执行测试用例'''
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        msg = tx['error_msg']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam2 = json.JSONDecoder().decode(tx['params'])

        if flag == 1:
            headers2['Authorization'] = ''
        if flag == 2:
            reqParam2['project_id'] = projectId
            reqParam2['volumes_name'] = volumeIds
            reqParam2['snapshot_name'] = instanceSnapInfo['snapshot_name']

        logger.info("*******测试数据： " + str(reqParam2))
        r = requests.post(url=reqUrl2, headers=headers2, json=reqParam2)
        result2 = r.json()
        logger.info("*******返回数据： " + str(result2))
        self.assertEqual(result2['code'], code)
        if result2['code'] != 0:
            self.assertEqual(result2['message'], msg)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************回滚云组件快照接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)

    @classmethod
    def tearDownClass(cls) -> None:
        headers3 = {'Content-Type': 'application/json',
                   'Authorization': token}
        reqUrl3 = logoutUrl
        res = requests.get(reqUrl3,headers=headers3)
        resJson = res.json()
        if resJson['code'] == 0:
            logger.info("**********************************************完成teardown class，退出登录**********************************************")

__generateTestCases(restoreInstanceSnap, "restoreInstanceSnap", "snapsMagData.xlsx", "restoreInstanceSnap")

if __name__ == '__main__':
    unittest.main()
