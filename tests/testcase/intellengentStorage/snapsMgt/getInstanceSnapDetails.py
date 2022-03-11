# -*- coding: utf-8 -*-
# @Time: 2022/01/13 10:53
# @Author: Leona
# @File: getInstanceSnapDetails.py


import unittest
import requests
import json
from configs.urlConfigs import instanceSnap,logoutUrl
from lib.PanaCubeCommon import login
from lib.PanacubeCommonQuery import getLatestInstanceSnap
from lib.generateTestCases import __generateTestCases
from lib.log import logger

"""
智能存储》快照管理》获取云组件快照详情信息
"""

class getInstanceSnapDetails(unittest.TestCase):
    '''获取智能存储》快照管理》获取云组件快照详情信息'''
    @classmethod
    def setUpClass(cls) -> None:
        logger.info(
            "**********************************************开始setupClass，进行登录**********************************************")
        global token, instanceSnapInfo
        token = login()
        projectId="4a18d8c090b74481952fa52f6967d5ed"
        instanceSnapInfo = getLatestInstanceSnap(projectId)

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************获取云组件快照详情接口开始****************")
        headers = {'Content-Type': 'application/json',
                   'Authorization': token
                   }
        reqUrl = instanceSnap + '/' + str(instanceSnapInfo['server_id']) + '/' + str(instanceSnapInfo['snapshot_name'])
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        logger.info("*******测试数据： " + str(reqParam))
        if flag == 1:
            headers['Authorization'] = ''
        r = requests.get(url=reqUrl, headers=headers, data=reqParam)
        result = r.json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************获取云组件快照详情接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("*" * 80)

    @classmethod
    def tearDownClass(cls) -> None:
        reqUrl = logoutUrl
        headers = {'Content-Type': 'application/json',
                   'Authorization': token}
        res = requests.get(reqUrl, headers=headers)
        resJson = res.json()
        if resJson['code'] == 0:
            logger.info(
                "**********************************************完成teardown class，退出登录**********************************************")

__generateTestCases(getInstanceSnapDetails, "getInstanceSnapDetails", "snapsMagData.xlsx", "getInstanceSnapDetails")

if __name__ == '__main__':
    unittest.main()
