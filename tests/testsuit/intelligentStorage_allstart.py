import unittest
import time
import os.path
import sys
basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(basedir)
from lib import send_email
from lib import HTMLTestRunner3
print(sys.path)


"""unittest.defaultTestLoader(): defaultTestLoader()类，
通过该类下面的discover()方法可自动根据测试目录start_dir匹配查找测试用例文件（testcase*.py），
并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover"""
suite = unittest.defaultTestLoader.discover(basedir + '/tests/testcase/intellengentStorage', pattern='*.py')

# filePath = basedir + "/reports/storageEngineReport.html"
# fp = open(filePath, 'wb')#
# """生成报告的Title,描述"""
# runner = HTMLTestRunner3.HTMLTestRunner(stream=fp, title='【QA环境】智能存储模块功能：接口测试报告', description='测试用例执行结果如下所示')
# runner.run(suite)
# fp.close()

report_file = basedir + "/reports/storageEngineReport.html"
with open(report_file,'wb') as rf:
    runner = HTMLTestRunner3.HTMLTestRunner(stream=rf,title='【QA环境】智能存储模块接口测试报告',description='测试用例结果如下所示：')
    runner.run(suite)

time.sleep(5)
send_email.send_mail_report("【QA环境】智能存储模块功能：接口测试报告")