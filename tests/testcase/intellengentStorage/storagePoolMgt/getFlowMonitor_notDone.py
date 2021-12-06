# -*- coding: utf-8 -*-
# @Time: 2021/12/03 10:46
# @Author: Leona
# @File: getFlowMonitor_notDone.py

import unittest
import requests
import json
import datetime
from configs.urlConfigs import storageFlowMonitor,logoutUrl
from lib.PanaCubeCommon import login
from lib.PanacubeCommonQuery import getNonDefaultPool
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
获取智能存储》存储池管理》存储池监控信息
"""


class getFlowMonitor(unittest.TestCase):
    """获取智能存储》存储池管理》管理》存储池监控信息"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token
        token = login()

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************获取存储流量监控接口开始****************")
        headers ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        msg = tx ['error_msg']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqUrl = storageFlowMonitor
        reqParam = json.JSONDecoder().decode(tx['params'])
        reqParam['end_time'] = datetime.datetime.now()
        #开始时间为当前时间往前推30分钟
        reqParam['start_time'] = reqParam['end_time'] - datetime.timedelta(minutes=30)
        logger.info("*******测试数据： " + str(reqParam))
        projectInfo = getNonDefaultPool()
        projectId = projectInfo[0]
        if flag == 1:
            headers['Authorization'] = ''
        headers['PROJECT-ID'] = projectId
        r = requests.get(url=reqUrl, headers=headers,data=reqParam)
        result = r.json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        if code!= 0:
            self.assertEqual(result['message'], msg)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************获取存储流量监控接口结束****************")

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

__generateTestCases(getFlowMonitor, "getFlowMonitor", "storagePoolMagData.xlsx", "getFlowMonitor")

if __name__ == '__main__':
    unittest.main()
