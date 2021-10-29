# coding:utf-8
# Author: Candy
import os
from lib import readexceldata
from configs.config import datapath

''''
1、写一个testcase 生成报告后，会有一个case的执行状态记录。
这样我们写一个登录功能的自动化用例，只写一个case显然是不行的，测试用例要满足他的覆盖度，所以我们需要写多个用例。
但是对于同样的功能，我们用例脚本体现出来的只有输入的参数值不一样，其它操作都是一样的。
2、这时候一个用例写一个test_case_login()的脚本，但是我们又想在报告中单独记录每一个case的执行状态，不得写多个重复的方法。 
如： test_case_login_1() test_case_login_2() test_case_login_3() 这样执行完成后，使用unittest的进行生成测试报告，对每一个test_case都能记录执行状态。
3、但是代码太过冗余，内容太过笨重。 或许此时我们可以仅写一个test case并用内嵌循环来进行，但是会出现一个问题，就是其中一个出了错误，很难从测试结果里边看出来。
4、 问题的关键在于是否有办法根据输入参数的不同组合产生出对应的test case。 
比如我5组数据，就应该有5个test_case_login，上面我已经说过不适合直接写5个test_case_login，那么应该怎么做呢？ 
一种可能的思路是不利用unittest.TestCase这个类框中的test_成员函数的方法，而是自己写runTest这个成员函数，那样会有一些额外的工作，而且看起来不是那么“智能”，
5、 如果目的是让框架自动调用test_case自然的思路就是：
• 利用setattr来自动为已有的TestCase类添加成员函数 
• 为了使这个方法凑效，需要用类的static method来生成decorate类的成员函数，并使该函数返回一个test函数对象出去 
• 在某个地方注册这个添加test成员函数的调用(只需要在实际执行前就可以，可以放在模块中自动执行亦可以手动调用)
'''

"""类的实例、被测试的接口名称、测试数据文件名、测试数据表单名称"""
def __generateTestCases (instanse, inerfaceName, tesDataName, sheetName):
    file = os.path.join(datapath, tesDataName)
    data_list = readexceldata.excel_to_list(file, sheetName)
    for i in range(len(data_list)):
        setattr(instanse, 'test_'+inerfaceName+'_%s'%(str(data_list[i]["test_num"]))+'_%s' % (str(data_list[i]["test_name"])), instanse.getTestFunc(data_list[i]))