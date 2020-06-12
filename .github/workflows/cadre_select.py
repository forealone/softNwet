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


zbzz80h = p_data.loc[p_data[(p_data['出生年份'] >= 1980) & (p_data['干部类型'] == '总部正职')].index, ['部门名称','职务','人员姓名']]

zbzz80h.shape[0]

text1 = pd.DataFrame([('一、80后总部一把手有%d人。' %zbzz80h.shape[0]),
        ('人员清单：')])

sheet1_merge = pd.concat([text1,zbzz80h], axis=0, ignore_index=False, sort=False)

text2 = pd.DataFrame([('（一）党委班子情况。申万宏源党委目前班子成员共%d人，平均年龄%f岁，其中70后%d人，占比f%%%；党委班子成员均为中共党员，均取得硕士以上学历或学位。')])
p_data.loc[p_data[p_data['公司领导类别1'] == '集团和证券公司党委班子'].index,['部门名称','职务','人员姓名','年龄']]

pt_output = pd.ExcelWriter(r'E:\1-统计\%s\raw\结构统计表-其他数据分析.xlsx' %date)
sheet1_merge.to_excel(pt_output, sheet_name='80后一把手', index=False, header=False)
pt_output.save()
