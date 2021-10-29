# -*- coding = utf-8 -*-
# @author = Leona

'''
配置发送邮件、访问数据库、日志等功能
'''

import os
import logging
import pymysql


"""项目路径"""
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""测试数据路径"""
datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'datafiles')
"""日志路径"""
logpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'logs')


"""数据库配置"""
panacube = dict(host='192.168.5.172', user='root', passwd='P@ssw0rd', port=3306,db='panacube4', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
panastor = dict(host='192.168.5.172', user='root', passwd='P@ssw0rd', port=3306,db='panastor', charset='utf8', cursorclass=pymysql.cursors.DictCursor)

"""邮件配置"""
sender = 'Cherry_Leejj@163.com'      #发件人
receiver = 'lijj@udsafe.com.cn'  #收件人

server = 'smtp.163.com'   #邮件服务器
emailusername = 'Cherry_Leejj@163.com'   #邮箱账号
emailpassword = 'CherryLeejj789'  #登陆邮箱的授权码，是授权码，不是邮箱密码



"""日志配置"""
logging.basicConfig(level=logging.DEBUG,    #log level
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s', #log格式
                    datefmt='%y-%m-%d %H:%M',  #日期格式
                    filename=os.path.join(logpath, 'log.txt'), #日志输出文件
                    filemode='a')  # 追加模式
