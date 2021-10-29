# -*- coding: utf-8 -*-
# @Time: 2021/10/18 18:01
# @Author: Leona
# @File: send_email1.py

import smtplib
import zipfile
import sys
import os
from email.mime.text import MIMEText               #发送纯文本信息
from email.mime.multipart import MIMEMultipart     #发送带附件的信息
from email.header import Header                    #导入配置库
from configs.config import basedir                 #导入项目路径
from configs import config                         #导入配置文件

"""1、压缩文件"""
def cr_zip(outputName, inputPath):
    '''将inputPath路径下的文件压缩成名字为outputName的文件，放到outputpath目录下'''
    outputPath = inputPath + outputName
    filelist = []
    isfp = os.path.basename(inputPath)
    if isfp:
        print("%s is not path" % inputPath)
        sys.exit(0)
    else:
        for root,subdirs, files in os.walk(inputPath):
            for file in files:
                filelist.append(os.path.join(root,file))

    zf = zipfile.ZipFile(outputPath,'w',zipfile.ZIP_DEFLATED)
    for f in filelist:
        zf.write(f)
    zf.close()

"""2、发送邮件"""
def send_mail_report(title):
    '''1-获取测试报告邮件服务器，发件人、收件人、发件人账号等信息'''
    sender = config.sender                 #发件人
    receiver = config.receiver             #收件人
    #第三方SMTP服务器
    server = config.server                 #设置服务器信息
    username = config.emailusername        #设置邮箱用户名
    password = config.emailpassword        #设置邮箱密码

    '''2、获取最新的测试报告'''
    reportPath = config.basedir + "/report/"
    newReport = ""
    for root, subdirs,files in os.walk(reportPath):
        for file  in files:
            if os.path.splitext(file)[1] == ".html":     #判断该目录下的文件扩展名是否为html
                newReport = file

    '''2.1、调佣cr_zip()方法，将报告压缩一下'''
    cr_zip('TestReport.zip',basedir+"/report/")

    '''3、生成邮件的内容'''
    msg = MIMEMultipart()     #创建一个带附件的实例
    msg["subject"] = title    #邮件主题
    msg["from"] = Header(sender,"utf-8")
    msg["to"] = Header(",".join(receiver),"utf-8")
    with open(os.path.join(reportPath,newReport),'rb') as f:
        mailbody = f.read()
    html = MIMEText(mailbody,_subtype="html",_charset="utf-8")
    msg.attach(html)

    """4、将测试报告压缩文件添加到邮件附件"""
    att = MIMEText(open(basedir+'/report/'+ 'TestReport.zip','rb').read(),'base64','utf-8')
    att["Conten-Type"] = 'application/octet-stream'      #application/octet-stream: 二进制流数据（如常见的文件下载）
    att.add_header("Content-Disposition","attachment",filename="TestReport.zip") #filename为附件名
    msg.attach(att)

    """5、发送邮件"""
    try:
        smtp = smtplib.SMTP()
        smtp.connect(server,25)  # 25为SMTP的端口号
        smtp.login(username,password)  #登录到邮件服务器
        smtp.sendmail(sender,receiver.split(','),msg.as_string())
        smtp.close()
        print("*************邮件发送成功*************")
    except smtplib.SMTPException:
        print("*************Error: 无法发送邮件*************")

# if __name__ == '__main__':
#     cr_zip("TestReport.zip",basedir+'/report/')
#     print(basedir+'/report/')
#     send_mail_report("Panacube4.0_API_TestReport")






