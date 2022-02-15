# -*- coding: utf-8 -*-
# @Time: 2022/02/15 11:20
# @Author: Leona
# @File: getPubNetIPList.py

import unittest
import requests
import json
from configs.urlConfigs import pubNetIP,logoutUrl
from lib.PanaCubeCommon import login
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
获取云中心》网络管理》公网IP列表信息
"""


class getPubNetIPList(unittest.TestCase):
    """获取云中心》网络管理》公网IP列表信息"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token
        token = login()

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************获取公网IP列表接口开始****************")
        headers ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqUrl = pubNetIP 
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        logger.info("*******测试数据： " + str(reqParam))
        if flag == 1:
            headers['Authorization'] = ''
        r = requests.get(url=reqUrl, headers=headers,data=reqParam)
        result = r.json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************获取公网IP列表接口结束****************")

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
        res = requests.get(reqUrl,headers=headers)
        resJson = res.json()
        if resJson['code'] == 0:
            logger.info("**********************************************完成teardown class，退出登录**********************************************")

__generateTestCases(getPubNetIPList, "getPubNetIPList", "netMgtData.xlsx", "getPubNetIPList")

if __name__ == '__main__':
    unittest.main()
