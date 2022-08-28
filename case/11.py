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
#    @Time : 2022/8/29 0:46
#    @FIle： 11.py
#    @Software: PyCharm
from util.find_case import findCase
from util.make_ddt import MakeDdt

casepath = findCase(__file__, 'login.yml')
test_cases = MakeDdt(casepath).makeData_V2()
print(test_cases)
print(type(test_cases))