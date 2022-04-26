# -*- coding: utf-8 -*-
# @Time: 2022/4/1 14:06
# @Author: Leona
# @File: materials.py

import requests
import random

def creMaterial(no,sProject, rProject):
    creaMaterialUrl = 'http://192.168.4.145:5559/materials/'
    headers = {"Content-Type":"applicaton/json"}
    reqParam ={
    "project_id":sProject,
    "name":"Material"+str(no),
    "data":genData(rProject)
}
    res = requests.post(headers=headers, url=creaMaterialUrl,json=reqParam,verify=False).json()
    if res['code'] == 0:
        print("材料创建成功")
    else:
        print("材料创建失败")

def batchCreMaterial(n,sProject,rProject):
    for i in range(n):
        creMaterial(i,sProject,rProject)


def genData(rProject):
    data = []
    rowRange = 5
    columnRange = 9
    for i in range(1, rowRange):
        for j in range(1, columnRange):
            item = {
            "row": i,
            "column": j,
            "name":"row"+ str(i) + "colume" + str(j) +"name" ,
            "content":"row"+ str(i) + "colume" + str(j) +"content" ,
            "project_id": str(rProject)
        }
            data.append(item)
    return data

#genData(86)
creMaterial(31,87,86)
# batchCreMaterial(25,87,86)
