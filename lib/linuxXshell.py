# -*- coding: utf-8 -*-
# @Time: 2021/11/4 16:56
# @Author: Leona
# @File: linuxXshell.py

import paramiko
#定义SSH连接方法
def conSSH(hostname,port,username,password,cmd):
    #定义连接重试次数
    try_times = 3
    try:
        #实例化一个SSHClient对象
        ssh = paramiko.SSHClient()
        #自动添加策略，保存服务器的主机名和秘钥信息，如果不添加，那么不再本地know_hosts文件中记录的主机将无法连接
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #连接SSH服务器，传参为： 服务器地址，端口，用户名，密码
        ssh.connect(hostname=hostname,port=port, username=username,password=password)
        #打开一个channel并执行命令
        stdin, stdout, stderr = ssh.exec_command(cmd)
        #打印执行结果到控制台
        print((stdout.read().decode('utf-8')))
        #将结果写入到sshRes.txt文件中
        # with open('sshRes.txt','a+') as res:
        #     res.write(stdout.read().decode('utf-8'))
        #关闭SSHClient连接
        ssh.close()
    except Exception as e:
        if try_times != 0:
            print('连接%s失败， 进行重试' % hostname)
            try_times -= 1
        else:
            print('连接3次失败， 结束程序')
            exit(1)

if __name__ == '__main__':
    #conSSH(hostname,port,username,password,cmd):
    # conSSH("192.168.5.172",22, "root","Admin@9000", "lsscsi")
    # conSSH("192.168.5.172",22, "root","Admin@9000", "df -h")
    # conSSH("192.168.5.172",22, "root","Admin@9000", "vgs")
    conSSH("192.168.2.169", 22, "root", "123456", "lsscsi")

