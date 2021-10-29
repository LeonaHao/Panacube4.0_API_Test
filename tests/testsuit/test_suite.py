# -*- coding: utf-8 -*-
# @Time: 2021/10/18 17:49
# @Author: Leona
# @File: test_suite.py

import unittest
import os
import time
from lib.HTMLTestRunner3 import HTMLTestRunner
from lib import send_email1

def myrunner():
    #生成报告文件的参数
    basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    #discover 这个方法可以递归地去识别路径下所有符合pattern的文件，将这些文件加入套件
    suite = unittest.defaultTestLoader.discover(basedir+ '/tests/testcase/',pattern='*.py')

    #生成报告文件的参数
    report_title = 'Panacube4.0 接口自动化测试结果'    #报告名称
    des = "饼图统计测试情况"                           #报告描述
    report_file = basedir + '/report/testsuit.html'   #报告文件
    with open(report_file,'wb') as report:
        runner = HTMLTestRunner(stream=report,title=report_title, description=des)
        runner.run(suite)
    report.close()

    #发送报告到邮箱
    time.sleep(1)
    send_email1.cr_zip('Panacube4_API_TestReport.zip',basedir+'/report/')
    send_email1.send_mail_report("【QA-Panacube4-API-test】")

