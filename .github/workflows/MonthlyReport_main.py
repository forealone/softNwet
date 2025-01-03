# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 10:27:15 2021

@author: User
"""

import re

date = input('输入月度统计表的年月，(格式：YYYYMM):')
while re.match(r'\d{4}(1[0-2]{1}$|0[0-9]{1}$)', date) == None:
    date = input('输入的年月有误，请按格式重新输入6位年月，(格式：YYYYMM):')

f1 = open(r"E:\23-个人\month.txt",'w')
f1.write('date = "%s"' %date)
f1.close()