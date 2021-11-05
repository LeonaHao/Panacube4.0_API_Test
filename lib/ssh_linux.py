# -*- coding: utf-8 -*-
# @Time: 2021/11/4 15:43
# @Author: Leona
# @File: ssh_linux.py

from time import *
import paramiko

#定义一个类，表示一台远端的linux虚机
class SSH_Linux(object):
    # 通过IP， 用户名，密码，超时时间初始化一个远程Linux主机
    def __init__(self,ip, username, password, timeout=30):
        self.ip = ip
        self.username =username
        self.password = password
        self.timeout = timeout
        #transport和channel
        self.t = ''
        self.chan = ''
        #链接失败的重试次数
        self.try_times = 3

    #连接远程主机
    def connect(self):
        while True:
            #链接过程中可能会抛出异常，比如网络不通，链接超时
            try:
                self.t = paramiko.Transport(sock=(self.ip,22))
                self.t.connect(username=self.username,password=self.password)
                self.chan = self.t.open_session()
                self.chan.settimeout(self.timeout)
                self.chan.get_pty()
                self.chan.invoke_shell()
                #如果没有抛异常，则说明链接成功，直接返回
                print("链接%s成功" % self.ip)
                # 接收到的网络数据解码为str
                print(self.chan.recv(65535)).decode('utf-8')
                return
            except Exception as e1:
                if self.try_times != 0:
                    print('链接%s失败，进行重试' % self.ip)
                    self.try_times -= 1
                else:
                    print('重试3次失败，结束程序')
                    exit(1)

    #关闭连接
    def closeConn(self):
        self.chan.close()
        self.t.close()

    #发送要执行的命令
    def sendCmd(self,cmd):
        cmd += '\r'
        result = ''
        #发送要执行的命令
        self.chan.send(cmd)
        #回显很长的命令可能执行较久，通过循环分批次取回回显。执行成功返回true，失败返回false
        while True:
            sleep(0.5)
            ret = self.chan.recv(65535)
            ret = ret.decode('utf-8')
            result += ret
            return result


if __name__ == '__main__':
    host = SSH_Linux('192.168.5.172','root','Cl0ud!P@ssw0rd')
    host.connect()
    def input_cmd(str):
        return input(str)
    tishi_msg = "输入命令： "
    while True:
        msg = input(tishi_msg)
        if msg == "exit":
            host.closeConn()
            break
        else:
            res = host.sendCmd(msg)
            data = res.replace(res.split("\n")[-1],"")
            tishi_msg = res.split("\n")[-1]
            print(res.split("\n")[-1] + data.strip("\n"))


