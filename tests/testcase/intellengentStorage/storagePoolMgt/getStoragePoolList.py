#coding=utf-8
import unittest
import requests
import json
from configs.urlConfigs import storagePoolListUrl
from lib.PanaCubeCommon import login
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
获取存储池列表信息
"""


class GetStoragePoolList(unittest.TestCase):
    """获取智能存储》存储池管理》存储池列表信息"""


    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************获取存储池管理列表接口开始****************")
        headers ={'Content-Type':'application/json',
                  'Authorization': login()}
        reqUrl = storagePoolListUrl
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
        logger.info("****************获取存储池管理列表接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)


__generateTestCases(GetStoragePoolList, "GetStoragePoolList", "storagePoolMagData.xlsx", "storagePoolList")

if __name__ == '__main__':
    unittest.main()
