# -*- coding: utf-8 -*-
# @Time: 2021/12/09 14:29
# @Author: Leona
# @File: detachDataDisk.py

import unittest
import requests
import json
import urllib3
import time
from configs.urlConfigs import cloudDisk,cloudDiskDetach,forceDelCD, logoutUrl
from lib.PanaCubeCommon import login
from lib.PanacubeCommonQuery import getAttachableDisk
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
智能存储》云硬盘管理》卸载数据盘
"""


class detachDataDisk(unittest.TestCase):
    """智能存储》云硬盘管理》加载数据盘"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token, projectId, projectName
        token = login()
        projectId="f4fb64c3ff9d4c1186c9d3502af4020d"
        projectName="TestPool"

        '''先创建1个云硬盘'''
        global headers
        headers1 ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqParam1 = {
            "name":"CloudDisk4Detach",
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

        '''获取可加载的数据盘信息'''
        global attachAbleDiskInfo
        attachAbleDiskInfo = getAttachableDisk(projectId)

        '''加载云硬盘'''
        reqParam2 ={
            "volume":attachAbleDiskInfo['diskId'],
            "action":"attach",
            "path":"/mnt/test_"+attachAbleDiskInfo['diskName'],
            "instance":[
                attachAbleDiskInfo['vmId']
            ],
            "project_id":projectId,
            "project_name":projectName
        }
        reqUrl2 = cloudDiskDetach
        r = requests.post(url=reqUrl2, headers=headers1, json=reqParam2).json()

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************卸载数据盘列表接口开始****************")
        headers3 ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqUrl3 = cloudDiskDetach

        '''执行卸载数据盘的测试用例'''
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        msg = tx['error_msg']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam3 = json.JSONDecoder().decode(tx['params'])
        reqParam3['project_id'] = attachAbleDiskInfo['projectId']
        reqParam3['project_name'] = attachAbleDiskInfo['projectName']
        if flag == 1:
            headers3['Authorization'] = ''
        if flag == 2:
            reqParam3['volume'] = attachAbleDiskInfo['diskId']
            reqParam3['instance'] = [attachAbleDiskInfo['vmId']]
        logger.info("*******测试数据： " + str(reqParam3))
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        r = requests.post(url=reqUrl3, headers=headers3, json=reqParam3)
        result3 = r.json()
        logger.info("*******返回数据： " + str(result3))
        time.sleep(3)
        self.assertEqual(result3['code'], code)
        if result3['code'] != 0:
            self.assertEqual(result3['message'], msg)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************卸载数据盘列表接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)

    @classmethod
    def tearDownClass(cls) -> None:
        headers4 = {'Content-Type': 'application/json',
                   'Authorization': token}
        '''环境清理删除创建的云硬盘'''
        reqUrl4 = forceDelCD
        reqParam4 ={
            "disk_ids":[
                attachAbleDiskInfo['diskId']
            ],
            "project_id": projectId,
            "project_name":projectName
        }
        # print("***************强制删除参数为： {}***".format(reqParam4))
        result4 = requests.post(url=reqUrl4, headers=headers4, json=reqParam4,verify=False).json()
        # print(result4)
        reqUrl5 = logoutUrl
        res = requests.get(reqUrl5,headers=headers4)
        resJson = res.json()
        if resJson['code'] == 0:
            logger.info("**********************************************完成teardown class，退出登录**********************************************")

__generateTestCases(detachDataDisk, "detachDataDisk", "cloudDiskMagData.xlsx", "detachDataDisk")

if __name__ == '__main__':
    unittest.main()
