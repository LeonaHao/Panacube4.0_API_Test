# -*- coding: utf-8 -*-
# @Time: 2022/02/14 16:29
# @Author: Leona
# @File: stopS3Service.py

import unittest
import requests
import json
from configs.urlConfigs import magServiceUrl, logoutUrl
from lib.PanaCubeCommon import login,getShareService
from lib.PanacubeCommonQuery import getS3
from random import randint
import uuid
from lib.generateTestCases import __generateTestCases
from lib.log import logger


"""
智能存储》服务管理》关闭S3服务
"""


class stopS3Service(unittest.TestCase):
    """智能存储》服务管理》关闭S3服务"""
    @classmethod
    def setUpClass(cls) -> None:
        logger.info("**********************************************开始setupClass，进行登录**********************************************")
        global token,projectId,projectName,s3Service,nodeList
        token = login()
        #该projectId为默认池的id
        projectId = 'ef7107f3b443415da1ccc56fa8e726b2'
        projectName = u'默认池'

        headers = {'Content-Type': 'application/json',
                   'Authorization': token
                   }
        # 查看s3服务状态，如果已经是开启状态，先关闭S3服务
        s3Service = getShareService()
        nodeList =[]
        statusList = []
        if s3Service[0]['name']=='S3':
            #查看节点状态
            for item in s3Service[0]['status']:
                nodeList.append(item['node'])
                statusList.append(item['status'])
                if item['status'] == 0:
                    print("***********{}节点上的s3服务目前处于关闭状态**********".format(item['node']))
                    reqUrl = magServiceUrl
                    reqParam = {
                        "action":"start",
                        "params":{
                            "node":nodeList
                        },
                        "project_id":projectId,
                        "project_name":projectName
                    }
                    r = requests.post(url=reqUrl, headers=headers, json=reqParam)
                    print("开启S3服务成功")
                elif item['status'] ==1:
                    print("***********{}节点上的s3服务目前处于开启状态**********".format(item['node']))

                else:
                    logger.info("***********s3服务状态异常**********")



    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************关闭S3服务接口开始****************")
        headers1 = {'Content-Type': 'application/json',
                    'Authorization': token
                    }
        reqUrl = magServiceUrl
        caseNum = tx['test_num']
        caseName = tx['test_name']
        code = tx['code']
        flag = tx['flag']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        reqParam = json.JSONDecoder().decode(tx['params'])
        reqParam['params']['node'] = nodeList

        if flag == 1:
            headers1['Authorization'] = ''
        logger.info("*******测试数据： " + str(reqParam))
        r = requests.post(url=reqUrl, headers=headers1, json=reqParam, verify=False)
        result = r.json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************关闭S3服务接口结束****************")

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

__generateTestCases(stopS3Service, "stopS3Service", "serviceMagData.xlsx", "stopS3Service")

if __name__ == '__main__':
    unittest.main()
