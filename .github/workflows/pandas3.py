# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 14:43:33 2019

@author: User
"""

#同比、环比、上年度（年底）比较

import pandas as pd


cadre_data_io_this = pd.io.excel.ExcelFile(r'E:\1-统计\201911\raw\干部信息统计汇总表.xls')
cadre_data_this = pd.read_excel(cadre_data_io_this,sheet_name='按干部类型')
cadre_data_io_this.close()

cadre_data_io_that = pd.io.excel.ExcelFile(r'E:\1-统计\201910\raw\干部信息统计汇总表.xls')
cadre_data_that = pd.read_excel(cadre_data_io_that,sheet_name='按干部类型')
cadre_data_io_that.close()

#（本期数-上期数）/上期数×100%
cadre_data_this.shape

i = 1
while i < 15:
    cadre_data_this['%s环比' %cadre_data_this.columns[i]] = (cadre_data_this.iloc[:,i] - cadre_data_that.iloc[:,i]) / cadre_data_that.iloc[:,i]
    
    i += 1

j = 15
while j < 29:
    cadre_data_this[cadre_data_this.columns[j]] = cadre_data_this[cadre_data_this.columns[j]].apply(lambda x: format(x, '.2%'))
    cadre_data_this.loc[:, cadre_data_this.columns[j]] = cadre_data_this[cadre_data_this.columns[j]].replace('nan%', '0')
    cadre_data_this.loc[:, cadre_data_this.columns[j]] = cadre_data_this[cadre_data_this.columns[j]].replace('inf%', '-（上期为0）')
    cadre_data_this.loc[:, cadre_data_this.columns[j]] = cadre_data_this[cadre_data_this.columns[j]].replace('0.00%', '0')
    j += 1

cadre_data_output = pd.ExcelWriter(r'C:\Users\User\Desktop\环比表.xls')
cadre_data_this.to_excel(cadre_data_output, sheet_name='按干部类型', index=False)

cadre_data_output.save()