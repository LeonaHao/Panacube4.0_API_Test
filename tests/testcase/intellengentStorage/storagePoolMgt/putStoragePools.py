# -*- coding: utf-8 -*-
# @Time: 2021/11/04 17:49
# @Author: Leona
# @File: putStoragePools.py

import unittest
import requests
import json
from configs.urlConfigs import storagePoolUrl,logoutUrl
from lib.PanaCubeCommon import login
from lib.PanacubeCommonQuery import getNonDefaultPool
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
获取智能存储》存储池管理》系统配额信息
"""


class putStoragePools(unittest.TestCase):
    """获取智能存储》概况中的存储信息"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token
        token = login()

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************配置业务池接口开始****************")
        headers ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqUrl = storagePoolUrl
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        msg = tx['error_msg']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")

        reqParam = json.JSONDecoder().decode(tx['params'])
        storagePoolInfo = getNonDefaultPool()
        projectId = storagePoolInfo[0]
        storageLimit = storagePoolInfo[2]
        reqParam['project_id']= projectId
        reqParam['storage_limit']=storageLimit
        logger.info("*******测试数据： " + str(reqParam))
        if flag == 1:
            headers['Authorization'] = ''
        r = requests.put(url=reqUrl, headers=headers,json=reqParam)
        result = r.json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        if result['code']!=0:
            self.assertEqual(result['message'], msg)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************配置业务池接口结束****************")

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

__generateTestCases(putStoragePools, "putStoragePools", "storagePoolMagData.xlsx", "putStoragePools")

if __name__ == '__main__':
    unittest.main()
