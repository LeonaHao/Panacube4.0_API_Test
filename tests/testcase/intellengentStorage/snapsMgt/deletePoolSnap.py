# -*- coding: utf-8 -*-
# @Time: 2021/12/10 15:31
# @Author: Leona
# @File: deletePoolSnap.py

import unittest
import requests
import json
import urllib3
import time
from configs.urlConfigs import poolSnap,delPoolSnap, logoutUrl
from lib.PanaCubeCommon import login
from lib.PanacubeCommonQuery import getLatestPoolSnap
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
智能存储》快照管理》删除业务池快照
"""


class deletePoolSnap(unittest.TestCase):
    """智能存储》快照管理》删除业务池快照"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token, projectId, projectName
        token = login()
        projectId="ddac080c671b473e885714538fd1ed6e"
        projectName="LeonaTestPool1125"
        "创建1个业务池快照"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }
        reqParam = {
            "name": "poolSnap4" + str(projectName),
            "project_id": projectId
        }
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        poolRes = requests.post(url=poolSnap, headers=headers, json=reqParam, verify=False).json()
        time.sleep(5)

        '''获取最新的业务池快照信息'''
        global poolSnapInfo
        poolSnapInfo = getLatestPoolSnap(projectId)

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************删除业务池快照接口开始****************")
        headers2 ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqUrl2 = delPoolSnap

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
            reqParam2['ids'] = [poolSnapInfo['snapshot_id']]
        logger.info("*******测试数据： " + str(reqParam2))
        r = requests.delete(url=reqUrl2, headers=headers2, json=reqParam2)
        result2 = r.json()
        logger.info("*******返回数据： " + str(result2))
        self.assertEqual(result2['code'], code)
        if result2['code'] != 0:
            self.assertEqual(result2['message'], msg)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************删除业务池快照接口结束****************")

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

__generateTestCases(deletePoolSnap, "deletePoolSnap", "snapsMagData.xlsx", "deletePoolSnap")

if __name__ == '__main__':
    unittest.main()