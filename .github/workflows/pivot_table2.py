# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:20:17 2019

@author: User
"""

import pandas as pd
import numpy as np

#数据处理(注意每月修改日期)
p_data = pd.read_excel(r'E:\1-统计\201910\raw\干部信息明细表（编辑）.xlsx')

p_data['政治面貌分类'] = '群众'
p_data.loc[p_data[p_data['政治面貌'].str.contains('民盟|民革|民建|民进|农工党|致公党|九三学社|民主自治同盟')].index,['政治面貌分类']] = '民主党派'
p_data.loc[p_data[p_data['政治面貌'].str.contains('中共')].index,['政治面貌分类']] = '中共党员'

p_data['最高学历'].fillna('硕士研究生',inplace=True)
p_data.loc[p_data[p_data['最高学历'].str.contains('专科|中专|高中|初中|小学|职高|技校|中技')].index,['最高学历']] = '大学专科及以下'
p_data.loc[p_data[p_data['最高学历'].str.contains('本科')].index,['最高学历']] = '大学本科'
p_data.loc[p_data[p_data['最高学历'].str.contains('硕士|研究生毕业班')].index,['最高学历']] = '硕士研究生'
p_data.loc[p_data[p_data['最高学历'].str.contains('博士')].index,['最高学历']] = '博士研究生'

p_data['年龄']=p_data['年龄'].astype('float')
p_data.dtypes

#第一张表（按部门类型统计性别、政治面貌、学历、年龄）
pt_xb = pd.pivot_table(p_data,index=['部门类型'],columns=['性别'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zzmm = pd.pivot_table(p_data,index=['部门类型'],columns=['政治面貌分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zgxl = pd.pivot_table(p_data,index=['部门类型'],columns=['最高学历'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_nljg = pd.pivot_table(p_data,index=['部门类型'],columns=['年龄段'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_pjnl = pd.pivot_table(p_data,index=['部门类型'],values=['年龄'],aggfunc={'年龄':np.mean}, fill_value=0, margins=True)
pt_pjnl.rename(columns={'年龄':'平均年龄'},inplace=True)

pt_xb.columns.levels[1]  #透视表第二列索引
pt_xb.columns = pt_xb.columns.droplevel(level=0)  #删除透视表第一列索引
pt_zzmm.columns = pt_zzmm.columns.droplevel(level=0)
pt_zgxl.columns = pt_zgxl.columns.droplevel(level=0)
pt_nljg.columns = pt_nljg.columns.droplevel(level=0)
del pt_zzmm['All']
del pt_zgxl['All']
del pt_nljg['All']

pt_merge = pd.merge(pt_xb,pt_zzmm,how='left',left_index=True,right_index=True)
pt_merge = pd.merge(pt_merge,pt_zgxl,how='left',left_index=True,right_index=True)
pt_merge = pd.merge(pt_merge,pt_nljg,how='left',left_index=True,right_index=True)
pt_merge = pd.merge(pt_merge,pt_pjnl,how='left',left_index=True,right_index=True)

pt_merge.fillna(0,inplace=True)
pt_merge.rename(columns={'All':'人数'}, index={'All':'合计'}, inplace=True)
row = ['公司领导','集团公司业务总部','集团公司职能总部','证券公司业务总部','证券公司党群部门','分公司','子公司','营业部','合计']
pt_merge = pt_merge.reindex(row)  #行索引排序（部门类型）
col = ['人数','男','女','中共党员','民主党派','群众','博士研究生','硕士研究生','大学本科','大学专科及以下','35岁及以下','36-45岁','45岁以上','平均年龄']
pt_merge = pt_merge.reindex(columns=col)  #列索引排序



#输出(注意每月修改日期)
pt_output = pd.ExcelWriter(r'E:\1-统计\201910\raw\干部信息统计汇总表test.xls')
pt_merge.to_excel(pt_output, sheet_name='按部门统计')
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
