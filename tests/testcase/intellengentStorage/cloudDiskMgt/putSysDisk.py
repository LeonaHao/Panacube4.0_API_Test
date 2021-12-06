# -*- coding: utf-8 -*-
# @Time: 2021/12/06 14:29
# @Author: Leona
# @File: putSysDisk.py

import unittest
import requests
import json
import urllib3
from configs.urlConfigs import cloudDisk,logoutUrl
from lib.PanaCubeCommon import login,getSysDiskInfo
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
智能存储》云硬盘管理》编辑系统盘信息
"""


class putSysDisk(unittest.TestCase):
    """智能存储》云硬盘管理》编辑系统盘信息"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token
        token = login()

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************编辑系统盘列表接口开始****************")

        headers ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqUrl = cloudDisk

        '''查找要编辑的系统盘数据'''
        reqUrl1 = cloudDisk + '?page=1&size=10&info=sys'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result1 = requests.get(url=reqUrl1, headers=headers, verify=False).json()
        if len(result1['data']) != 0:
            sysDiskInfo = result1['data'][0]
            sysDiskId = sysDiskInfo['id']
            sysDisksize = sysDiskInfo['size']
            sysDisktype = sysDiskInfo['disk_type']
            sysDiskStatus = sysDiskInfo['disk_status']
            sysDiskCreTime = sysDiskInfo['created_time']
            sysDiskSnap = sysDiskInfo['is_snapshoted']
            projectName = sysDiskInfo['project_name']
            projectId = sysDiskInfo['project_id']
            poolName = sysDiskInfo['pool_name']

            '''执行更新系统盘的测试用例'''

            caseNum = tx['test_num']
            caseName = tx['test_name']
            code = tx['code']
            msg = tx['error_msg']
            flag = tx['flag']
            logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
            reqParam = json.JSONDecoder().decode(tx['params'])
            reqParam['id'] = sysDiskId
            reqParam['size'] = sysDisksize
            reqParam['disk_type'] = sysDisktype
            reqParam['disk_status'] = sysDiskStatus
            reqParam['created_time'] = sysDiskCreTime
            reqParam['is_snapshoted'] = sysDiskSnap
            reqParam['project_name'] = projectName
            reqParam['project_id'] = projectId
            reqParam['pool_name'] = poolName
            logger.info("*******测试数据： " + str(reqParam))
            if flag == 1:
                headers['Authorization'] = ''
            r = requests.put(url=reqUrl + '/'+ str(reqParam['id']) , headers=headers,json=reqParam)
            result = r.json()
            logger.info("*******返回数据： " + str(result))
            self.assertEqual(result['code'], code)
            if result['code']!=0:
                self.assertEqual(result['message'],msg)
            logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
            logger.info("****************编辑系统盘列表接口结束****************")

        else:
            logger.info("**************没有系统盘信息******************")

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

__generateTestCases(putSysDisk, "putSysDisk", "cloudDiskMagData.xlsx", "putSysDisk")

if __name__ == '__main__':
    unittest.main()
