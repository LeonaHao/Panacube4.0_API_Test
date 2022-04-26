# -*- coding: utf-8 -*-
# @Time: 2022/1/13 15:48
# @Author: Leona
# @File: putCloudDiskSnap.py

import unittest
import requests
import json
from uuid import uuid4
from configs.urlConfigs import diskSnap,logoutUrl
from lib.PanaCubeCommon import login
from lib.PanacubeCommonQuery import getLatestDataDisk,getLatestDiskSnap
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
智能存储》快照管理》编辑云硬盘快照名称
"""


class putCloudDiskSnap(unittest.TestCase):
    """智能存储》快照管理》编辑云硬盘快照名称"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token, projectId, projectName
        token = login()
        projectId="eec452bb462b4edead7e7750394bcb3e"
        projectName="LeonaTestPool"
    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************编辑云硬盘快照名称接口开始****************")
        headers2 ={'Content-Type':'application/json',
                  'Authorization': token
                   }

        '''执行测试用例'''
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        msg = tx['error_msg']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")


        '''获取最新的云硬盘快照信息'''
        diskSanpInfo = getLatestDiskSnap(projectId)
        if flag == 0:
            reqUrl2 = diskSnap + '/' + str(uuid4())
        else:
            reqUrl2 = diskSnap + '/' + diskSanpInfo['id']
        logger.info("*******请求地址： " +str(reqUrl2))

        if flag == 1:
            headers2['Authorization'] = ''

        reqParam2 = json.JSONDecoder().decode(tx['params'])
        logger.info("*******测试数据： " + str(reqParam2))

        r = requests.put(url=reqUrl2, headers=headers2, json=reqParam2)
        result2 = r.json()
        logger.info("*******返回数据： " + str(result2))
        self.assertEqual(result2['code'], code)
        if result2['code'] != 0:
            self.assertEqual(str(result2['message']), msg)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************编辑云硬盘快照名称接口结束****************")

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

__generateTestCases(putCloudDiskSnap, "putCloudDiskSnap", "snapsMagData.xlsx", "putCloudDiskSnap")

if __name__ == '__main__':
    unittest.main()