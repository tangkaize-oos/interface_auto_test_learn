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
#    @Time : 2022/8/28 23:58
#    @FIle： Test_demo.py
#    @Software: PyCharm
import requests

from util.make_ddt import MakeDdt
from util.find_case import findCase

casepath = findCase(__file__, 'login.yml')
test_cases = MakeDdt(casepath).makeData_V2()
print(test_cases)


class TestDemo():

    def test_balanceUser(self):
        response = requests.get(
            url="https://www.baidu.com/sugrec?prod=pc_his&from=pc_web&json=1&sid=36557_36462_37114_36885_36803_37137_26350_37210_37196_37227&hisdata=&_t=1661704400192&bs=2131&csor=0")

        print(response.json())
        assert 200 == response.status_code

# if __name__ == '__main__':
