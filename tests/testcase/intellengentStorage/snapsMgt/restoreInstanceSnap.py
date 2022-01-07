# -*- coding: utf-8 -*-
# @Time: 2022/01/07 14:02
# @Author: Leona
# @File: restoreInstanceSnap.py

import unittest
import requests
import json
import urllib3
import time
import random
from configs.urlConfigs import cloudInstanceSnap, logoutUrl
from lib.PanaCubeCommon import login
from lib.PanacubeCommonQuery import getInsAndDisk,getLatestInstanceSnap
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
智能存储》快照管理》回滚云组件快照
"""


class restoreInstanceSnap(unittest.TestCase):
    """智能存储》快照管理》回滚业云组件快照"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token, projectId, projectName
        token = login()
        projectId="c732c22666064375904c357bbecfeb1a"
        projectName="HJp0_hash"


        '''获取可创建云组件快照的云硬盘及组件信息'''
        global insAndDiskInfo
        insAndDiskInfo = getInsAndDisk(projectId)

        "创建1个云组件快照"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }
        reqParam = {
            "snapshot_name":"snap4_" +  insAndDiskInfo['vmName'] +"_" + str(random.randint(1,100)),
            "volumes_ids":[insAndDiskInfo['diskId']],
            "project_id":projectId,
            "project_name":projectName
}
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        reqUrl1 = cloudInstanceSnap + str(insAndDiskInfo['vmId']) + '/snapshots'
        print(reqUrl1)
        insSnapRes = requests.post(url=reqUrl1, headers=headers, json=reqParam, verify=False).json()
        time.sleep(15)


    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************回滚云组件快照接口开始****************")
        headers2 ={'Content-Type':'application/json',
                  'Authorization': token
                   }
        reqUrl2 = cloudInstanceSnap + str(insAndDiskInfo['vmId']) + '/restore'
        logger.info("*******请求地址： " +str(reqUrl2))

        '''执行测试用例'''
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        msg = tx['error_msg']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam2 = json.JSONDecoder().decode(tx['params'])
        reqParam2['project_id'] = projectId
        reqParam2['volumes_name'] = [insAndDiskInfo['diskId']]
        reqParam2['snapshot_name'] = getLatestInstanceSnap(projectId)['snapshot_name']
        if flag == 1:
            headers2['Authorization'] = ''
        if flag == 2:
            reqParam2['snapshot_name'] = ""
        if flag == 3:
            reqParam2['volumes_name'] = []
        if flag == 4:
            reqParam2['project_id'] = ""

        logger.info("*******测试数据： " + str(reqParam2))
        r = requests.post(url=reqUrl2, headers=headers2, json=reqParam2)
        result2 = r.json()
        logger.info("*******返回数据： " + str(result2))
        self.assertEqual(result2['code'], code)
        if result2['code'] != 0:
            self.assertEqual(result2['message'], msg)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************回滚云组件快照接口结束****************")

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

__generateTestCases(restoreInstanceSnap, "restoreInstanceSnap", "snapsMagData.xlsx", "restoreInstanceSnap")

if __name__ == '__main__':
    unittest.main()
