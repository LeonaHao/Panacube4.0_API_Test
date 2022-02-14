# -*- coding: utf-8 -*-
# @Time: 2022/02/14 12:09
# @Author: Leona
# @File: getServiceList.py

import unittest
import requests
import json
from configs.urlConfigs import serviceUrl,logoutUrl
from lib.PanaCubeCommon import login
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
获取智能存储》服务管理》服务列表信息
"""


class getServiceList(unittest.TestCase):
    """获取智能存储》服务管理》服务列表信息"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token,projectId
        token = login()
        #该projectId为默认池的id
        projectId = 'ef7107f3b443415da1ccc56fa8e726b2'

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************获取共享列表接口开始****************")

        headers ={'Content-Type':'application/json',
                  'Authorization': token,
                  'PROJECT-ID': projectId
                   }
        reqUrl = serviceUrl
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
        logger.info("****************获取共享列表接口结束****************")

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

__generateTestCases(getServiceList, "getServiceList", "serviceMagData.xlsx", "getServiceList")

if __name__ == '__main__':
    unittest.main()
