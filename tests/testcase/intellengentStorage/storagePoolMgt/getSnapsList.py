# -*- coding: utf-8 -*-
# @Time: 2021/12/03 10:09
# @Author: Leona
# @File: getCloudDiskList.py

import unittest
import requests
import json
from configs.urlConfigs import poolSnap,instanceSnap,diskSnap,logoutUrl
from lib.PanaCubeCommon import login
from lib.PanacubeCommonQuery import getNonDefaultPool
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
获取智能存储》存储池管理》系统配额信息
"""


class getSnapsList(unittest.TestCase):
    """获取智能存储》存储池管理》管理》快照管理中的信息"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token
        token = login()

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************获取快照列表接口开始****************")

        headers ={'Content-Type':'application/json',
                  'Authorization': token
                   }

        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        msg = tx ['error_msg']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        if flag == 2 or caseNum == '004':
            reqUrl = poolSnap
        if flag == 3:
            reqUrl = instanceSnap
        if flag == 4:
            reqUrl = diskSnap
        reqParam = json.JSONDecoder().decode(tx['params'])
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
        logger.info("****************获取快照列表接口结束****************")

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

__generateTestCases(getSnapsList, "getSnapsList", "storagePoolMagData.xlsx", "getSnapsList")

if __name__ == '__main__':
    unittest.main()
