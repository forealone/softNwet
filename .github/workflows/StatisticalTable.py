# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:20:17 2019

@author: User
"""

import pandas as pd
import numpy as np
import os
import re
from countdown import countdown

print('即将开始制作月报-集团和证券公司干部结构统计表... ')
seconds = 3
countdown(seconds)

date = '999999'
try:
    with open(r"E:\23-个人\month.txt",'r') as file_to_read:
        s = file_to_read.read()
    exec(s)
except:
    print('未知异常')

while re.match(r'\d{4}(1[0-2]{1}$|0[0-9]{1}$)', date) == None:
    date = input('输入的年月有误，请按格式重新输入6位年月，(格式：YYYYMM):')
    
print('请检查文件目录是否正确、确保目录下有以下文件：\n “E:\\1-统计\\%s\\raw\\干部信息明细表（数据清洗）.xlsx” ' %date)
countdown(seconds)
if os.access(r'E:\1-统计\%s\raw\干部信息明细表（数据清洗）.xlsx' %date, os.F_OK):
    pass
else:
    input('【E:\\1-统计\\%s\\raw\\干部信息明细表（数据清洗）.xlsx】不存在，是否继续？（按回车键继续...） \n' %date)
p_data = pd.read_excel(r'E:\1-统计\%s\raw\干部信息明细表（数据清洗）.xlsx' %date)

#年龄字段格式修改，便于计算
p_data['年龄']=p_data['年龄'].astype('float')
p_data.dtypes

#定义各类统计口径下的类别排序，以便后面使用（按实际情况更新）
row1 = ['公司正职', '公司副职', '总部正职', '总部副职', '总部助理', '二级总部正职', '二级总部副职', '二级总部助理', '分公司正职', '分公司副职', '分公司助理', '子公司正职', '子公司副职', '子公司助理', '总部二级部门经理', '分公司二级部门经理','子公司二级部门经理', '营业部正职', '营业部正职（卫星）', '营业部副职', '营业部助理','转任干部','非行政职务','合计']
row2 = ['总部正职', '总部副职', '总部助理', '二级总部正职', '二级总部副职', '二级总部助理', '分公司正职', '分公司副职', '分公司助理', '子公司正职', '子公司副职', '子公司助理', '总部二级部门经理', '分公司二级部门经理','子公司二级部门经理', '营业部正职', '营业部正职（卫星）', '营业部副职', '营业部助理', '合计']
row3 = ['集团公司总部领导班子','集团公司总部二级部门经理','证券公司事业部总部领导班子','证券公司事业部总部二级部门经理','分公司本部领导班子','分公司二级部门经理','子公司领导班子','子公司二级部门经理','合计']
row4 = ['公司领导','总部业务部门','总部职能部门','总部党群部门','分公司','子公司','营业部','其他','合计']
row5_1 = ['集团和证券公司党委班子']
row5_2 = ['集团公司经营班子','证券公司经营班子']
row6 = None
col1 = ['人数','男','女','中共党员','民主党派','群众','博士研究生','硕士研究生','大学本科','大学专科及以下','35岁及以下','36-45岁','45岁以上','平均年龄','1年内退休','到退岗年龄']
col2 = ['人数','男','女','中共党员','民主党派','群众','博士研究生','硕士研究生','大学本科','大学专科及以下','35岁及以下','36-45岁','45岁以上','平均年龄']

def PivotTable(row, col, data=p_data, summary_type=['干部类型']):  #定义处理pivottable的函数，默认按照干部类型汇总
    pt_xb = pd.pivot_table(data,index=summary_type,columns=['性别'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
    pt_zzmm = pd.pivot_table(data,index=summary_type,columns=['政治面貌分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
    pt_zgxl = pd.pivot_table(data,index=summary_type,columns=['最高学历分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
    pt_nljg = pd.pivot_table(data,index=summary_type,columns=['年龄段'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
    pt_pjnl = pd.pivot_table(data,index=summary_type,values=['年龄'],aggfunc={'年龄':np.mean}, fill_value=0, margins=True)
    pt_pjnl.rename(columns={'年龄':'平均年龄'},inplace=True)
    pt_tx = pd.pivot_table(data,index=summary_type,columns=['退休标识'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0 ,dropna=False, margins=True)
    pt_tg = pd.pivot_table(data,index=summary_type,columns=['退岗标识'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, dropna=False, margins=True)

    pt_xb.columns.levels[1]  #透视表第二列索引
    pt_xb.columns = pt_xb.columns.droplevel(level=0)  #删除透视表第一列索引
    pt_zzmm.columns = pt_zzmm.columns.droplevel(level=0)
    pt_zgxl.columns = pt_zgxl.columns.droplevel(level=0)
    pt_nljg.columns = pt_nljg.columns.droplevel(level=0)
    pt_tx.columns = pt_tx.columns.droplevel(level=0)
    pt_tg.columns = pt_tg.columns.droplevel(level=0)

    del pt_zzmm['All']
    del pt_zgxl['All']
    del pt_nljg['All']
    del pt_tx['All']
    del pt_tg['All']

    pt_merge = pd.merge(pt_xb,pt_zzmm,how='left',left_index=True,right_index=True)
    pt_merge = pd.merge(pt_merge,pt_zgxl,how='left',left_index=True,right_index=True)
    pt_merge = pd.merge(pt_merge,pt_nljg,how='left',left_index=True,right_index=True)
    pt_merge = pd.merge(pt_merge,pt_pjnl,how='left',left_index=True,right_index=True)
    pt_merge = pd.merge(pt_merge,pt_tx,how='left',left_index=True,right_index=True)
    pt_merge = pd.merge(pt_merge,pt_tg,how='left',left_index=True,right_index=True)

    pt_merge.fillna(0,inplace=True)
    pt_merge.rename(columns={'All':'人数'}, index={'All':'合计'}, inplace=True)
    pt_merge = pt_merge.reindex(row)  #行索引排序（干部类型）
    pt_merge = pt_merge.reindex(columns=col)  #列索引排序
    
    return pt_merge

#第一、二张表（按干部类型统计性别、政治面貌、学历、年龄）
pt_merge1 = PivotTable(row1, col1)

p_data2 = p_data.drop(p_data[p_data['干部类型'].isin(['公司正职','公司副职','公司助理','公司总监','转任干部','非行政职务'])].index)
pt_merge2 = PivotTable(row2, col1, data=p_data2)


#第三张表（按总部级干部类别）
pt_merge3 = PivotTable(row3, col1, summary_type=['总部级干部类别'])

#第四张表（按部门类别）
pt_merge4 = PivotTable(row4, col1, summary_type=['部门类别'])

p_data4 = p_data.drop(p_data[p_data['干部类型'] == '其他'].index)
pt_merge4 = PivotTable(row4, col1, data=p_data4, summary_type=['部门类别'])

#第五张表（按公司领导类别1、公司领导类别2）
pt_merge5_1 = PivotTable(row5_1, col2, summary_type=['公司领导类别1'])

pt_merge5_2 = PivotTable(row5_2, col2, summary_type=['公司领导类别2'])

pt_merge5 = pd.concat([pt_merge5_1,pt_merge5_2], axis=0, ignore_index=False, sort=False)
pt_merge5.fillna(0,inplace=True)

#第六张表（按每个部门统计性别、政治面貌、学历、年龄）（有待研究multiindex的情况如何排序？）
pt_merge6 = PivotTable(row6, col1, summary_type=['组织','一级部门'])

#输出(注意每月修改日期)
print('将输出文件至目录E:\\1-统计\\%s\\raw\\' %date)
countdown(seconds)
pt_output = pd.ExcelWriter(r'E:\1-统计\%s\raw\集团和证券公司干部结构统计表raw.xls' %date)
pt_merge1.to_excel(pt_output, sheet_name='按干部类型')
pt_merge2.to_excel(pt_output, sheet_name='按干部类型（统计口径）')
pt_merge3.to_excel(pt_output, sheet_name='按总部级和部门经理级')
pt_merge4.to_excel(pt_output, sheet_name='按部门类别')
pt_merge5.to_excel(pt_output, sheet_name='按公司领导类别')
pt_merge6.to_excel(pt_output, sheet_name='按一级部门')
pt_output.save()

'''
按条件筛选
p_data_select = p_data['干部类型'].notnull() # Series类型 true与false的一列
p_data_select = p_data[p_data['干部类型'].notnull()] # DataFrame类型 按照year非空选择之后的结果
p_data_select = p_data[p_data['干部类型'].notnull()].values  #array
p_data_select = p_data[p_data['干部类型'] == '公司总监'][p_data['最高学历'] == '博士研究生']  #Dataframe
p_data_select.iloc[0,:]
p_data_select.T

'''

