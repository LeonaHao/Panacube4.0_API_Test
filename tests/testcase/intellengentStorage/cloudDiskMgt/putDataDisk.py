# -*- coding: utf-8 -*-
# @Time: 2021/12/06 17:29
# @Author: Leona
# @File: putDataDisk.py

import unittest
import requests
import json
import urllib3
from configs.urlConfigs import cloudDisk,logoutUrl
from lib.PanaCubeCommon import login
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
智能存储》云硬盘管理》编辑数据盘列表信息
"""


class putDataDisk(unittest.TestCase):
    """智能存储》云硬盘管理》编辑数据盘列表信息"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token
        token = login()

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************编辑数据盘列表接口开始****************")

        headers ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqUrl = cloudDisk

        '''获取数据盘信息'''
        reqUrl1 = cloudDisk + '?page=1&size=10&info=data'
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        result1 = requests.get(url=reqUrl, headers=headers, verify=False).json()
        # print(result1)
        if len(result1['data']) != 0:
            dataDiskInfo = result1['data'][0]
            dataDiskId = dataDiskInfo['id']
            dataDisksize = dataDiskInfo['size']
            dataDisktype = dataDiskInfo['disk_type']
            dataDiskStatus = dataDiskInfo['disk_status']
            dataDiskShareVol = dataDiskInfo['share_vol']
            dataDiskCreTime = dataDiskInfo['created_time']
            dataDiskSnap = dataDiskInfo['is_snapshoted']
            dataDiskAttachInstance = dataDiskInfo['instances']
            dataDiskAttachPath = dataDiskInfo['path']
            projectName = dataDiskInfo['project_name']
            projectId = dataDiskInfo['project_id']
            poolName = dataDiskInfo['pool_name']

            '''执行更新数据盘的测试用例'''
            caseNum = tx['test_num']
            caseName = tx['test_name']
            code = tx['code']
            msg = tx['error_msg']
            flag = tx['flag']
            logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
            reqParam = json.JSONDecoder().decode(tx['params'])
            reqParam['id'] = dataDiskId
            reqParam['size'] = dataDisksize
            reqParam['disk_type'] = dataDisktype
            reqParam['disk_status'] = dataDiskStatus
            reqParam['share_vol'] = dataDiskShareVol
            reqParam['created_time'] = dataDiskCreTime
            reqParam['is_snapshoted'] = dataDiskSnap
            reqParam['instances'] = dataDiskAttachInstance
            reqParam['path'] = dataDiskAttachPath
            reqParam['project_name'] = projectName
            reqParam['project_id'] = projectId
            reqParam['pool_name'] = poolName

            logger.info("*******测试数据： " + str(reqParam))
            if flag == 1:
                headers['Authorization'] = ''
            r = requests.put(url=reqUrl + '/' + str(reqParam['id']), headers=headers, json=reqParam)
            result = r.json()
            logger.info("*******返回数据： " + str(result))
            self.assertEqual(result['code'], code)
            if result['code'] != 0:
                self.assertEqual(result['message'], msg)
            logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
            logger.info("****************编辑数据盘列表接口结束****************")

        else:
            logger.info("**************没有数据盘信息******************")
            pass


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

__generateTestCases(putDataDisk, "putDataDisk", "cloudDiskMagData.xlsx", "putDataDisk")

if __name__ == '__main__':
    unittest.main()
