# -*- coding: utf-8 -*-
# @Time: 2022/01/13 11:02
# @Author: Leona
# @File: restoreCloudDiskSnap.py

import unittest
import requests
import json
import urllib3
import time
import random
from configs.urlConfigs import diskSnap, logoutUrl
from lib.PanaCubeCommon import login
from lib.PanacubeCommonQuery import getLatestDiskSnap
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
智能存储》快照管理》回滚数据盘快照
"""


class restoreCloudDiskSnap(unittest.TestCase):
    """智能存储》快照管理》回滚数据盘快照"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token, projectId, projectName
        token = login()
        projectId="4a18d8c090b74481952fa52f6967d5ed"
        projectName="LeonaTestPool0310"

        '''获取最新的数据盘快照信息'''
        global cloudDiskSnapInfo
        cloudDiskSnapInfo = getLatestDiskSnap(projectId)


    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************回滚数据盘快照接口开始****************")
        headers2 ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqUrl2 = diskSnap + '/' + str(cloudDiskSnapInfo['id'])
        logger.info("*******请求地址： " +str(reqUrl2))

        '''执行测试用例'''
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        msg = tx['error_msg']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam2 = json.JSONDecoder().decode(tx['params'])
        reqParam2['project_id'] = projectId
        reqParam2['project_name'] = projectName
        if flag == 1:
            headers2['Authorization'] = ''
        if flag == 2:
            reqParam2['project_id'] = ""
        if flag == 3:
            reqParam2['project_name'] = ""

        logger.info("*******测试数据： " + str(reqParam2))
        r = requests.post(url=reqUrl2, headers=headers2, json=reqParam2)
        result2 = r.json()
        logger.info("*******返回数据： " + str(result2))
        self.assertEqual(result2['code'], code)
        if result2['code'] != 0:
            self.assertEqual(result2['message'], msg)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************回滚数据盘快照接口结束****************")

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

__generateTestCases(restoreCloudDiskSnap, "restoreCloudDiskSnap", "snapsMagData.xlsx", "restoreCloudDiskSnap")

if __name__ == '__main__':
    unittest.main()
