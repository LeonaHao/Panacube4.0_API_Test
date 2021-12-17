# -*- coding: utf-8 -*-
# @Time: 2021/12/17 10:58
# @Author: Leona
# @File: genCidr.py

# 首先引入netaddr
import netaddr
def genCidr():
    #创建一个空的列表，用来装cidr地址
    iplist = []
    # 确定起始和结尾IP，无论多复杂都可以转换
    startip = '192.16.16.10'
    endip = '192.16.246.246'
    #生成一个cidr列表，列表中元素类型为： class 'netaddr.ip.IPNetwork'
    cidrs = netaddr.iprange_to_cidrs(startip, endip)
    #通过enumerate函数，将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，最终返回 enumerate(枚举) 对象
    for k, v in enumerate(cidrs):
        iplist.append(str(v))
    return (iplist)

if __name__ == '__main__':
    print(genCidr())