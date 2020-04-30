# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 09:56:29 2020

@author: User
"""
import pandas as pd

#数据处理(注意每月修改日期)
date = input('输入月度统计表的年月，(格式：YYYYMM):')
print('E:\\1-统计\\%s\\raw\\ \n' %date)
input('请检查文件目录是否正确，确保目录下有以下文件：\n “干部信息明细表（数据清洗）.xlsx” \n 按回车键继续...')

p_data = pd.read_excel(r'E:\1-统计\%s\raw\干部信息明细表（数据清洗）.xlsx' %date)


zbzz80h = p_data.loc[p_data[(p_data['出生年份'] >= 1980) & (p_data['干部类型'] == '总部正职')].index, ['人员姓名','部门名称','职务']]

zbzz80h.shape[0]

print('一、80后总部一把手有%d人。' %zbzz80h.shape[0])
print('人员清单： \n',zbzz80h)


