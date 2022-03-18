# -*- coding: utf-8 -*-
# @Time: 2022/1/13 13:38
# @Author: Leona
# @File: deleteCloudDiskSnap.py

import unittest
import requests
import json
import time
from uuid import uuid4
from configs.urlConfigs import diskSnap,delDiskSnap,logoutUrl
from lib.PanaCubeCommon import login
from lib.PanacubeCommonQuery import getLatestDataDisk,getLatestDiskSnap
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
智能存储》快照管理》删除云硬盘快照
"""


class deleteCloudDiskSnap(unittest.TestCase):
    """智能存储》快照管理》删除云硬盘快照"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token, projectId, projectName
        token = login()
        projectId="0896b5ef96ce4471bc04a782085bbb98"
        projectName="LeonaTestPool0316"

        '''创建3个云硬盘快照用于删除'''
        headers1 ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        for i in range(1,4):
            reqParam1 = {
                "name":"cdSanp" + str(i),
                "description":"",
                "volume":getLatestDataDisk(projectId)['id']
            }
            r = requests.post(url=diskSnap, headers=headers1, json=reqParam1).json()
            time.sleep(5)

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************删除云硬盘快照接口开始****************")
        headers2 ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqUrl2 = delDiskSnap
        logger.info("请求地址为： {}".format(reqUrl2))

        '''执行测试用例'''
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        msg = tx['error_msg']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam2 = json.JSONDecoder().decode(tx['params'])

        diskSanpInfo = getLatestDiskSnap(projectId)
        reqParam2['ids'] = [diskSanpInfo['id']]
        reqParam2['project_id'] = projectId
        reqParam2['project_name'] = projectName

        if flag == 1:
            headers2['Authorization'] = ''
        if flag == 2:
            reqParam2['ids'] = []
        if flag == 3:
            reqParam2['project_id'] = ""
        if flag == 4:
            reqParam2['project_name'] = ""
        if flag == 5:
            reqParam2['ids'] = [str(uuid4())]
        logger.info("*******测试数据： " + str(reqParam2))

        r = requests.post(url=reqUrl2, headers=headers2, json=reqParam2)
        result2 = r.json()
        logger.info("*******返回数据： " + str(result2))
        self.assertEqual(result2['code'], code)
        if result2['code'] != 0:
            self.assertEqual(str(result2['message']), msg)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************删除云硬盘快照接口结束****************")

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

__generateTestCases(deleteCloudDiskSnap, "deleteCloudDiskSnap", "snapsMagData.xlsx", "deleteCloudDiskSnap")

if __name__ == '__main__':
    unittest.main()