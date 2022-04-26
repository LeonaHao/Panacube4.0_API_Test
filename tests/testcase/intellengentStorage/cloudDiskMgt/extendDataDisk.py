# -*- coding: utf-8 -*-
# @Time: 2021/12/09 11:07
# @Author: Leona
# @File: extendDataDisk.py

import unittest
import requests
import json
import urllib3
import time
from configs.urlConfigs import cloudDisk,forceDelCD, logoutUrl
from lib.PanaCubeCommon import login
from lib.PanacubeCommonQuery import getLatestDataDisk
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
智能存储》云硬盘管理》为数据盘扩容
"""


class extendDataDisk(unittest.TestCase):
    """智能存储》云硬盘管理》为数据盘创建快照"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token, projectId, projectName
        token = login()
        projectId="eec452bb462b4edead7e7750394bcb3e"
        projectName="LeonaTestPool"

        '''先创建1个云硬盘'''
        headers1 ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqParam1 = {
            "name":"CloudDisk4Extend",
            "size":"1",
            "disk_type": 0,
            "description": "",
            "compression": "off",
            "dedup": "off",
            "volblocksize": "512B",
            "share_vol": 1,
            "project_id": projectId,
            "project_name": projectName
        }
        result1 = requests.post(url=cloudDisk, headers=headers1, json=reqParam1, verify=False).json()
        time.sleep(5)

        '''获取用于扩容的数据盘信息'''
        global DataDiskId
        DataDiskId = getLatestDataDisk(projectId)['id']

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************数据盘扩容接口开始****************")
        headers2 ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqUrl2 = cloudDisk + '/'+str(DataDiskId)

        '''执行加载数据盘的测试用例'''
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        msg = tx['error_msg']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam2 = json.JSONDecoder().decode(tx['params'])
        reqParam2['volume'] = DataDiskId
        reqParam2['project_id'] = projectId
        reqParam2['project_name'] = projectName
        logger.info("*******测试数据： " + str(reqParam2))

        if flag == 1:
            headers2['Authorization'] = ''
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        r = requests.post(url=reqUrl2, headers=headers2, json=reqParam2)
        result2 = r.json()
        logger.info("*******返回数据： " + str(result2))
        self.assertEqual(result2['code'], code)
        if result2['code'] != 0:
            self.assertEqual(result2['message'],str(msg) )
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************数据盘扩容接口结束****************")

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
        '''环境清理删除创建的云硬盘'''
        reqUrl3 = forceDelCD
        reqParam3 ={
            "disk_ids":[
                DataDiskId
            ],
            "project_id": projectId,
            "project_name":projectName
        }
        # print("***************强制删除参数为： {}***".format(reqParam3))
        result3 = requests.post(url=reqUrl3, headers=headers3, json=reqParam3,verify=False).json()
        # print(result3)
        reqUrl4 = logoutUrl
        res = requests.get(reqUrl4,headers=headers3)
        resJson = res.json()
        if resJson['code'] == 0:
            logger.info("**********************************************完成teardown class，退出登录**********************************************")

__generateTestCases(extendDataDisk, "extendDataDisk", "cloudDiskMagData.xlsx", "extendDataDisk")

if __name__ == '__main__':
    unittest.main()
