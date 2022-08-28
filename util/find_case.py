#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    @Author : 李将
#
#              _____               ______
#     ____====  ]OO|_n_n__][.      |    |]
#    [________]_|__|________)<     
#     oo    oo  'oo OOOO-| oo\_   ~o~~~o~'
# +--+--+--+--+--+--+--+--+--+--+--+--+--+
#    @Time : 2022/8/29 0:17
#    @FIle： find_case.py
#    @Software: PyCharm
import os

"""
寻找case的路径
"""
def findCase(file, yml_file, n=1):
    path = os.path.dirname(file)
    if n > 0:
        n = n - 1
        casepath = findCase(path, yml_file, n)
    else:
        casepath = os.path.join(path, 'data', yml_file)

    return casepath