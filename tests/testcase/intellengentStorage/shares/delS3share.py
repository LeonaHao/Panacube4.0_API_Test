# -*- coding: utf-8 -*-
# @Time: 2022/01/21 15:29
# @Author: Leona
# @File: delS3Share.py

import unittest
import requests
import json
from configs.urlConfigs import shareUrl,shareDelUrl, logoutUrl
from lib.PanaCubeCommon import login
from lib.PanacubeCommonQuery import getS3
from random import randint
import uuid
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
删除智能存储》共享管理》S3共享信息
"""


class delS3Share(unittest.TestCase):
    """删除智能存储》共享管理》S3共享信息"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token,projectId,projectName,s3Info
        token = login()
        #该projectId为默认池的id
        projectId = 'ef7107f3b443415da1ccc56fa8e726b2'
        projectName = u'默认池'

        headers = {'Content-Type': 'application/json',
                   'Authorization': token
                   }
        # 如果有s3共享，直接使用现有s3共享，没有的话，创建一个s3共享
        s3Info = getS3()
        if not s3Info:
            reqUrl = shareUrl
            param4S3 = {
                "name": "s3share4CI" + str(randint(0, 10)),
                "s3": "yes",
                "port": str(randint(9000, 10000)),
                "access_key": "11112222",
                "secret_key": "11112222",
                "share_type": 2,
                "agree_type": [
                    "S3"
                ],
                "project_id": projectId,
                "project_name": projectName
            }
            res = requests.post(url=shareUrl, headers=headers, json=param4S3, verify=False).json()

    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************删除S3共享接口开始****************")
        headers1 = {'Content-Type': 'application/json',
                   'Authorization': token
                   }
        reqUrl = shareDelUrl
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])

        if flag == 1:
            headers1['Authorization'] = ''
        if flag ==2:
            reqParam['ids'] = [str(uuid.uuid4())]
        else:
            reqParam['ids'] = [getS3()['id']]
        logger.info("*******测试数据： " + str(reqParam))

        r = requests.delete(url=reqUrl, headers=headers1,json=reqParam)
        result = r.json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************删除S3共享接口结束****************")

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

__generateTestCases(delS3Share, "delS3Share", "sharesMagData.xlsx", "delS3Share")

if __name__ == '__main__':
    unittest.main()
