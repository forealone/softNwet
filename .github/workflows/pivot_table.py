# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:20:17 2019

@author: User
"""
input('即将开始制作月报-集团和证券公司干部结构统计表，按回车键继续...')

import pandas as pd
import numpy as np

#数据处理(注意每月修改日期)
date = input('输入月度统计表的年月，(格式：YYYYMM):')
print('E:\\1-统计\\%s\\raw\\ \n' %date)
input('请检查文件目录是否正确，确保目录下有以下文件：\n “干部信息明细表（编辑）.xlsx” \n 按回车键继续...')

p_data = pd.read_excel(r'E:\1-统计\%s\raw\干部信息明细表（编辑）.xlsx' %date)

#年龄字段格式修改，便于计算
p_data['年龄']=p_data['年龄'].astype('float')
p_data.dtypes

#第一张表（按干部类型统计性别、政治面貌、学历、年龄）
pt_xb = pd.pivot_table(p_data,index=['干部类型'],columns=['性别'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zzmm = pd.pivot_table(p_data,index=['干部类型'],columns=['政治面貌分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zgxl = pd.pivot_table(p_data,index=['干部类型'],columns=['最高学历分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_nljg = pd.pivot_table(p_data,index=['干部类型'],columns=['年龄段'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_pjnl = pd.pivot_table(p_data,index=['干部类型'],values=['年龄'],aggfunc={'年龄':np.mean}, fill_value=0, margins=True)
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
row = ['公司正职', '公司副职', '公司助理', '公司总监', '总部正职', '总部副职', '总部助理', '二级总部正职', '二级总部副职', '二级总部助理', '分公司正职', '分公司副职', '分公司助理', '子公司正职', '子公司副职', '子公司助理', '总部二级部门经理', '分公司二级部门经理', '营业部正职', '营业部正职（卫星）', '营业部副职', '营业部助理', '非行政职务','合计']
pt_merge = pt_merge.reindex(row)  #行索引排序（干部类型）
col = ['人数','男','女','中共党员','民主党派','群众','博士研究生','硕士研究生','大学本科','大学专科及以下','35岁及以下','36-45岁','45岁以上','平均年龄']
pt_merge = pt_merge.reindex(columns=col)  #列索引排序


#第二张表（按总部级干部类别）
pt_xb2 = pd.pivot_table(p_data,index=['总部级干部类别'],columns=['性别'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zzmm2 = pd.pivot_table(p_data,index=['总部级干部类别'],columns=['政治面貌分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zgxl2 = pd.pivot_table(p_data,index=['总部级干部类别'],columns=['最高学历分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_nljg2 = pd.pivot_table(p_data,index=['总部级干部类别'],columns=['年龄段'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_pjnl2 = pd.pivot_table(p_data,index=['总部级干部类别'],values=['年龄'],aggfunc={'年龄':np.mean}, fill_value=0, margins=True)
pt_pjnl2.rename(columns={'年龄':'平均年龄'},inplace=True)

pt_xb2.columns.levels[1]  #透视表第二列索引
pt_xb2.columns = pt_xb2.columns.droplevel(level=0)  #删除透视表第一列索引
pt_zzmm2.columns = pt_zzmm2.columns.droplevel(level=0)
pt_zgxl2.columns = pt_zgxl2.columns.droplevel(level=0)
pt_nljg2.columns = pt_nljg2.columns.droplevel(level=0)
del pt_zzmm2['All']
del pt_zgxl2['All']
del pt_nljg2['All']

pt_merge2 = pd.merge(pt_xb2,pt_zzmm2,how='left',left_index=True,right_index=True)
pt_merge2 = pd.merge(pt_merge2,pt_zgxl2,how='left',left_index=True,right_index=True)
pt_merge2 = pd.merge(pt_merge2,pt_nljg2,how='left',left_index=True,right_index=True)
pt_merge2 = pd.merge(pt_merge2,pt_pjnl2,how='left',left_index=True,right_index=True)

pt_merge2.fillna(0,inplace=True)
pt_merge2.rename(columns={'All':'人数'}, index={'All':'合计'}, inplace=True)
row = ['集团公司总部领导班子','证券公司事业部总部领导班子','分公司本部领导班子','子公司领导班子','合计']
pt_merge2 = pt_merge2.reindex(row)  #行索引排序（干部类型）
col = ['人数','男','女','中共党员','民主党派','群众','博士研究生','硕士研究生','大学本科','大学专科及以下','35岁及以下','36-45岁','45岁以上','平均年龄']
pt_merge2 = pt_merge2.reindex(columns=col)  #列索引排序

#第三张表（按部门类别）
pt_xb3 = pd.pivot_table(p_data,index=['部门类别'],columns=['性别'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zzmm3 = pd.pivot_table(p_data,index=['部门类别'],columns=['政治面貌分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zgxl3 = pd.pivot_table(p_data,index=['部门类别'],columns=['最高学历分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_nljg3 = pd.pivot_table(p_data,index=['部门类别'],columns=['年龄段'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_pjnl3 = pd.pivot_table(p_data,index=['部门类别'],values=['年龄'],aggfunc={'年龄':np.mean}, fill_value=0, margins=True)
pt_pjnl3.rename(columns={'年龄':'平均年龄'},inplace=True)

pt_xb3.columns.levels[1]  #透视表第二列索引
pt_xb3.columns = pt_xb3.columns.droplevel(level=0)  #删除透视表第一列索引
pt_zzmm3.columns = pt_zzmm3.columns.droplevel(level=0)
pt_zgxl3.columns = pt_zgxl3.columns.droplevel(level=0)
pt_nljg3.columns = pt_nljg3.columns.droplevel(level=0)
del pt_zzmm3['All']
del pt_zgxl3['All']
del pt_nljg3['All']

pt_merge3 = pd.merge(pt_xb3,pt_zzmm3,how='left',left_index=True,right_index=True)
pt_merge3 = pd.merge(pt_merge3,pt_zgxl3,how='left',left_index=True,right_index=True)
pt_merge3 = pd.merge(pt_merge3,pt_nljg3,how='left',left_index=True,right_index=True)
pt_merge3 = pd.merge(pt_merge3,pt_pjnl3,how='left',left_index=True,right_index=True)

pt_merge3.fillna(0,inplace=True)
pt_merge3.rename(columns={'All':'人数'}, index={'All':'合计'}, inplace=True)
row = ['公司领导','总部业务部门','总部职能部门','总部党群部门','分公司','子公司','营业部','合计']
pt_merge3 = pt_merge3.reindex(row)  #行索引排序（干部类型）
col = ['人数','男','女','中共党员','民主党派','群众','博士研究生','硕士研究生','大学本科','大学专科及以下','35岁及以下','36-45岁','45岁以上','平均年龄']
pt_merge3 = pt_merge3.reindex(columns=col)  #列索引排序

#第四张表（按公司领导类别1、公司领导类别2）
pt_xb4 = pd.pivot_table(p_data,index=['公司领导类别1'],columns=['性别'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zzmm4 = pd.pivot_table(p_data,index=['公司领导类别1'],columns=['政治面貌分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zgxl4 = pd.pivot_table(p_data,index=['公司领导类别1'],columns=['最高学历分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_nljg4 = pd.pivot_table(p_data,index=['公司领导类别1'],columns=['年龄段'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_pjnl4 = pd.pivot_table(p_data,index=['公司领导类别1'],values=['年龄'],aggfunc={'年龄':np.mean}, fill_value=0, margins=True)
pt_pjnl4.rename(columns={'年龄':'平均年龄'},inplace=True)

pt_xb4.columns.levels[1]  #透视表第二列索引
pt_xb4.columns = pt_xb4.columns.droplevel(level=0)  #删除透视表第一列索引
pt_zzmm4.columns = pt_zzmm4.columns.droplevel(level=0)
pt_zgxl4.columns = pt_zgxl4.columns.droplevel(level=0)
pt_nljg4.columns = pt_nljg4.columns.droplevel(level=0)
del pt_zzmm4['All']
del pt_zgxl4['All']
del pt_nljg4['All']

pt_merge4 = pd.merge(pt_xb4,pt_zzmm4,how='left',left_index=True,right_index=True)
pt_merge4 = pd.merge(pt_merge4,pt_zgxl4,how='left',left_index=True,right_index=True)
pt_merge4 = pd.merge(pt_merge4,pt_nljg4,how='left',left_index=True,right_index=True)
pt_merge4 = pd.merge(pt_merge4,pt_pjnl4,how='left',left_index=True,right_index=True)

pt_merge4.fillna(0,inplace=True)
pt_merge4.rename(columns={'All':'人数'}, index={'All':'合计'}, inplace=True)
pt_merge4 = pt_merge4.drop(['合计'])
col = ['人数','男','女','中共党员','民主党派','群众','博士研究生','硕士研究生','大学本科','大学专科及以下','35岁及以下','36-45岁','45岁以上','平均年龄']
pt_merge4 = pt_merge4.reindex(columns=col)  #列索引排序

pt_xb5 = pd.pivot_table(p_data,index=['公司领导类别2'],columns=['性别'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zzmm5 = pd.pivot_table(p_data,index=['公司领导类别2'],columns=['政治面貌分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zgxl5 = pd.pivot_table(p_data,index=['公司领导类别2'],columns=['最高学历分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_nljg5 = pd.pivot_table(p_data,index=['公司领导类别2'],columns=['年龄段'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_pjnl5 = pd.pivot_table(p_data,index=['公司领导类别2'],values=['年龄'],aggfunc={'年龄':np.mean}, fill_value=0, margins=True)
pt_pjnl5.rename(columns={'年龄':'平均年龄'},inplace=True)

pt_xb5.columns.levels[1]  #透视表第二列索引
pt_xb5.columns = pt_xb5.columns.droplevel(level=0)  #删除透视表第一列索引
pt_zzmm5.columns = pt_zzmm5.columns.droplevel(level=0)
pt_zgxl5.columns = pt_zgxl5.columns.droplevel(level=0)
pt_nljg5.columns = pt_nljg5.columns.droplevel(level=0)
del pt_zzmm5['All']
del pt_zgxl5['All']
del pt_nljg5['All']

pt_merge5 = pd.merge(pt_xb5,pt_zzmm5,how='left',left_index=True,right_index=True)
pt_merge5 = pd.merge(pt_merge5,pt_zgxl5,how='left',left_index=True,right_index=True)
pt_merge5 = pd.merge(pt_merge5,pt_nljg5,how='left',left_index=True,right_index=True)
pt_merge5 = pd.merge(pt_merge5,pt_pjnl5,how='left',left_index=True,right_index=True)

pt_merge5.fillna(0,inplace=True)
pt_merge5.rename(columns={'All':'人数'}, index={'All':'合计'}, inplace=True)
pt_merge5 = pt_merge5.drop(['合计'])
row = ['集团公司经营班子','证券公司经营班子']
pt_merge5 = pt_merge5.reindex(row)  #行索引排序（干部类型）
col = ['人数','男','女','中共党员','民主党派','群众','博士研究生','硕士研究生','大学本科','大学专科及以下','35岁及以下','36-45岁','45岁以上','平均年龄']
pt_merge5 = pt_merge5.reindex(columns=col)  #列索引排序

pt_merge5 = pd.concat([pt_merge4,pt_merge5], axis=0, ignore_index=False, sort=False)
pt_merge5.fillna(0,inplace=True)

#第五张表（按每个部门统计性别、政治面貌、学历、年龄）
pt_xb6 = pd.pivot_table(p_data,index=['组织','一级部门'],columns=['性别'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zzmm6 = pd.pivot_table(p_data,index=['组织','一级部门'],columns=['政治面貌分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_zgxl6 = pd.pivot_table(p_data,index=['组织','一级部门'],columns=['最高学历分类'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_nljg6 = pd.pivot_table(p_data,index=['组织','一级部门'],columns=['年龄段'],values=['工号'],aggfunc={'工号':'count'}, fill_value=0, margins=True)
pt_pjnl6 = pd.pivot_table(p_data,index=['组织','一级部门'],values=['年龄'],aggfunc={'年龄':np.mean}, fill_value=0, margins=True)
pt_pjnl6.rename(columns={'年龄':'平均年龄'},inplace=True)

pt_xb6.columns.levels[1]  #透视表第二列索引
pt_xb6.columns = pt_xb6.columns.droplevel(level=0)  #删除透视表第一列索引
pt_zzmm6.columns = pt_zzmm6.columns.droplevel(level=0)
pt_zgxl6.columns = pt_zgxl6.columns.droplevel(level=0)
pt_nljg6.columns = pt_nljg6.columns.droplevel(level=0)
del pt_zzmm6['All']
del pt_zgxl6['All']
del pt_nljg6['All']

pt_merge6 = pd.merge(pt_xb6,pt_zzmm6,how='left',left_index=True,right_index=True)
pt_merge6 = pd.merge(pt_merge6,pt_zgxl6,how='left',left_index=True,right_index=True)
pt_merge6 = pd.merge(pt_merge6,pt_nljg6,how='left',left_index=True,right_index=True)
pt_merge6 = pd.merge(pt_merge6,pt_pjnl6,how='left',left_index=True,right_index=True)

pt_merge6.fillna(0,inplace=True)
pt_merge6.rename(columns={'All':'干部人数'}, index={'All':'合计'}, inplace=True)
#pt_merge6.index
#pt_merge6 = pt_merge6.reindex(row)  #行索引排序 multiindex的情况如何排序？
col = ['干部人数','男','女','中共党员','民主党派','群众','博士研究生','硕士研究生','大学本科','大学专科及以下','35岁及以下','36-45岁','45岁以上','平均年龄']
pt_merge6 = pt_merge6.reindex(columns=col)  #列索引排序

#输出(注意每月修改日期)
print('E:\\1-统计\\%s\\raw\\' %date)
input('\n 将输出文件至上述目录，按回车键继续...')
pt_output = pd.ExcelWriter(r'E:\1-统计\%s\raw\干部信息统计汇总表.xls' %date)
pt_merge.to_excel(pt_output, sheet_name='按干部类型')
pt_merge2.to_excel(pt_output, sheet_name='按总部级干部类别')
pt_merge3.to_excel(pt_output, sheet_name='按部门类别')
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
