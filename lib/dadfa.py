
# -*- coding: utf-8 -*-
# @Time: 2022/1/19 16:46
# @Author: Leona
# @File: dadfa.py

from lib.PanacubeCommonQuery import getS3
s3Info = getS3()
if not s3Info:
    print('nothing')
else:
    print('ok')