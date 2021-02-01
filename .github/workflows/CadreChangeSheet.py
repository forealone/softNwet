# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:38:14 2019

@author: User
"""
input('即将开始制作月报-年度干部变动统计，按回车键继续... \n')

import pandas as pd
import re
import os

date = input('输入月度统计表的统计年月，用于命名导出文件，(格式：YYYYMM):')
while re.match(r'\d{4}(1[0-2]{1}$|0[0-9]{1}$)', date) == None:
    date = input('输入的年月有误，请按格式重新输入6位年月，(格式：YYYYMM):')
     
date_y = date[0:4]

input('确保目录下有以下文件：\n “E:\\组织部共享\\干部调整工作台账%s.xlsx” 。按回车键继续... \n' %date_y)
if os.access('E:\组织部共享\干部调整工作台账%s.xlsx' %date_y, os.F_OK):
    pass
else:
    print('E:\\组织部共享\\干部调整工作台账%s.xlsx' %date_y)
    input('上述目录文件不存在，是否继续？（按回车键继续...） \n')

data_io = pd.io.excel.ExcelFile(r'E:\组织部共享\干部调整工作台账%s.xlsx' %date_y)
data = pd.read_excel(data_io,sheet_name='干部调整情况', dtype={'工号':str})
data_io.close()

del data['管理权限']
del data['是否已上会']
del data['是否有业绩承诺']
del data['考察单位']
del data['是否已安排离任审计']
del data['是否向监管局报备']
del data['系统是否已调整']

data['发文文号'].fillna('暂未发文的予以剔除，不计入月报', inplace=True)
data = data.drop(data[data['发文文号'] == '暂未发文的予以剔除，不计入月报'].index)

#另一种常用统计口径
data['调整类别2'] = data['调整类别']
data.loc[data[data['调整类别'].isin(['平调','兼职','免兼职'])].index,['调整类别2']] = ['岗位调整']
data.loc[data[data['调整类别'].isin(['辞职','免职','降职','降级'])].index,['调整类别2']] = ['免职降职']
data['干部类别2'] = data['干部类别']
data.loc[data[data['干部类别'].str.contains('总部|分公司|子公司')].index,['干部类别2']] = ['总部、分（子）公司']
data.loc[data[data['干部类别'].str.contains('营业部')].index,['干部类别2']] = ['营业部干部']
data.loc[data[data['干部类别'].str.contains('二级部门')].index,['干部类别2']] = ['二级部门经理']

#匹配出生年月等信息，以便统计提聘引进干部年龄段
input('请检查文件目录是否正确、确保目录下有以下文件：\n “E:\\1-统计\\%s\\raw\\干部信息明细表（数据清洗）.xlsx” 。按回车键继续... \n' %date)
if os.access(r'E:\1-统计\%s\raw\干部信息明细表（数据清洗）.xlsx' %date, os.F_OK):
    pass
else:
    input('【E:\\1-统计\\%s\\raw\\干部信息明细表（数据清洗）.xlsx】不存在，是否继续？（按回车键继续...） \n' %date)
cadre_data = pd.read_excel(r'E:\1-统计\%s\raw\干部信息明细表（数据清洗）.xlsx' %date, sheet_name='干部信息明细表总表')
data_merge = pd.merge(data,cadre_data,on='工号',how='left')
data_merge['出生日期'].fillna('-',inplace=True)

'''
def alter_count(cadre):
    count_yj = data[(data['干部类别'] == cadre) & (data['调整类别'] == '引进')]['姓名'].count()
    count_tp = data[(data['干部类别'] == cadre) & (data['调整类别'] == '提聘')]['姓名'].count()
    count_pd = data[(data['干部类别'] == cadre) & (data['调整类别'] == '平调')]['姓名'].count()
    count_jj = data[(data['干部类别'] == cadre) & (data['调整类别'] == '降级')]['姓名'].count()
    count_mz = data[(data['干部类别'] == cadre) & ((data['调整类别'] == '免职') | (data['调整类别'] == '转岗'))]['姓名'].count()
    count_cz = data[(data['干部类别'] == cadre) & (data['调整类别'] == '辞职')]['姓名'].count()
    count_jz = data[(data['干部类别'] == cadre) & (data['调整类别'] == '兼职')]['姓名'].count()
    count_mjz = data[(data['干部类别'] == cadre) & (data['调整类别'] == '免兼职')]['姓名'].count()
    count_all = count_yj+count_tp+count_pd+count_jj+count_mz+count_cz+count_jz+count_mjz
    print('%s调整干部%s人。（包括引进%s人、提聘%s人、平调%s人、降职%s人、免职%s人、离职%s人、兼职%s人、免兼职%s人；）' %(cadre,count_all,count_yj,count_tp,count_pd,count_jj,count_mz,count_cz,count_jz,count_mjz))

def all_cadre_alter_count():
    alter_count('集团干部')
    alter_count('总部干部')
    alter_count('分公司干部')
    alter_count('子公司干部')
    alter_count('营业部正职')
    alter_count('营业部副职/卫星')
    alter_count('二级部门经理')

def summary_count():
    pass
'''
#透视图1
pivot_table = pd.pivot_table(data,index=['调整类别'],columns=['干部类别'], values=['姓名'], aggfunc={'姓名':'count'}, dropna=True, fill_value=0, margins=True, margins_name='合计') #去除columns中为空数据、用0填充空数字、展示汇总数all
pivot_table.columns = pivot_table.columns.droplevel(level=0) 
row = ['引进','提聘','平调','降级','免职','辞职','兼职','免兼职','合计']
pivot_table = pivot_table.reindex(row)  #行索引排序（干部类型）
col = ['公司领导','集团干部（总部）','集团干部（二级部门）','总部干部','分公司干部','子公司干部','营业部正职','营业部副职/卫星','二级部门经理','合计']
pivot_table = pivot_table.reindex(columns=col)  #列索引排序
pivot_table.fillna(0, inplace=True)

#透视图2
pivot_table2 = pd.pivot_table(data,index=['调整类别2'],columns=['干部类别2'], values=['姓名'], aggfunc={'姓名':'count'}, dropna=True, fill_value=0, margins=True, margins_name='合计') #去除columns中为空数据、用0填充空数字、展示汇总数all
pivot_table2.columns = pivot_table2.columns.droplevel(level=0) 
row = ['引进','提聘','岗位调整','免职降职','合计']
pivot_table2 = pivot_table2.reindex(row)  #行索引排序（干部类型）
col = ['公司领导','总部（分）子公司','二级部门经理','营业部干部','合计']
pivot_table2 = pivot_table2.reindex(columns=col)  #列索引排序
pivot_table2.fillna(0, inplace=True)


#证券公司总部分子公司干部变动人数加总
zqzb_sum = pivot_table.iloc[:,3] + pivot_table.iloc[:,4] + pivot_table.iloc[:,5]
#集团和证券公司总部分子公司干部变动人数加总
jtzqzb_sum = zqzb_sum + pivot_table.iloc[:,1]
jtzqzb_sum['引进']

#营业部干部变动人数加总
yyb_sum = pivot_table.iloc[:,6] + pivot_table.iloc[:,7]

#证券公司整体变动人数加总
zq_total = pivot_table.iloc[8,3] + pivot_table.iloc[8,4] + pivot_table.iloc[8,5] + pivot_table.iloc[8,6] + pivot_table.iloc[8,7] + pivot_table.iloc[8,8]

#集团公司整体变动人数加总
jt_total = pivot_table.iloc[8,1] + pivot_table.iloc[8,2]
#集团和证券公司整体变动人数加总
jtzq_total = jt_total + zq_total

#关于免职降级的详细统计（人员名单）
mz_yj = data[(data['调整类别'] == '免职') & (data['备注'].str.contains('另行|另有|赴香港工作|学习|转岗|退休|按规定转岗|违纪|纪委|平级|原职级不变|待定') != True)]
jj_yj = data[(data['调整类别'] == '降级') & (data['备注'].str.contains('另行|另有|赴香港工作|学习|转岗|退休|按规定转岗|违纪|纪委|平级|原职级不变|待定') != True)]
mz_jw = data[(data['调整类别'] == '免职') & (data['备注'].str.contains('违纪|纪委'))]
jj_jw = data[(data['调整类别'] == '降级') & (data['备注'].str.contains('违纪|纪委'))]

mz_yj_zb = mz_yj[mz_yj['干部类别'].isin(['集团干部（总部）','总部干部','分公司干部','子公司干部'])]
mz_yj_yyb = mz_yj[mz_yj['干部类别'].isin(['营业部正职','营业部副职/卫星'])]
mz_yj_bmjl = mz_yj[mz_yj['干部类别'].isin(['集团干部（二级部门）','二级部门经理'])]
jj_yj_zb = jj_yj[jj_yj['干部类别'].isin(['集团干部（总部）','总部干部','分公司干部','子公司干部'])]
jj_yj_yyb = jj_yj[jj_yj['干部类别'].isin(['营业部正职','营业部副职/卫星'])]
jj_yj_bmjl = jj_yj[jj_yj['干部类别'].isin(['集团干部（二级部门）','二级部门经理'])]
mz_jw_zb = mz_jw[mz_jw['干部类别'].isin(['集团干部（总部）','总部干部','分公司干部','子公司干部'])]
mz_jw_yyb = mz_jw[mz_jw['干部类别'].isin(['营业部正职','营业部副职/卫星'])]
mz_jw_bmjl = mz_jw[mz_jw['干部类别'].isin(['集团干部（二级部门）','二级部门经理'])]
jj_jw_zb = jj_jw[jj_jw['干部类别'].isin(['集团干部（总部）','总部干部','分公司干部','子公司干部'])]
jj_jw_yyb = jj_jw[jj_jw['干部类别'].isin(['营业部正职','营业部副职/卫星'])]
jj_jw_bmjl = jj_jw[jj_jw['干部类别'].isin(['集团干部（二级部门）','二级部门经理'])]

#关于引进、提聘干部年龄结构的分析
yj_all = data_merge[data_merge['调整类别'] == '引进']
yj_35 = data_merge[(data_merge['调整类别'] == '引进')&(data_merge['年龄段'] == '35岁及以下')]
tp_all = data_merge[data_merge['调整类别'] == '提聘']
tp_35 = data_merge[(data_merge['调整类别'] == '提聘')&(data_merge['年龄段'] == '35岁及以下')]

#生成一段文字描述
text = [('一、今年以来至本月底，共调整干部%d人。（不计公司领导调整）' %jtzq_total),
        ('集团公司调整干部%d人。（其中集团公司总部干部引进%d人、提聘%d人、平调%d人、降职%d人、免职%d人、离职%d人、兼职%d人、免兼职%d人；' %(jt_total,pivot_table.iloc[0,1],pivot_table.iloc[1,1],pivot_table.iloc[2,1],pivot_table.iloc[3,1],pivot_table.iloc[4,1],pivot_table.iloc[5,1],pivot_table.iloc[6,1],pivot_table.iloc[7,1])),
        ('集团公司二级部门经理引进%d人、提聘%d人、平调%d人、降职%d人、免职%d人、离职%d人、兼职%d人、免兼职%d人。）' %(pivot_table.iloc[0,2],pivot_table.iloc[1,2],pivot_table.iloc[2,2],pivot_table.iloc[3,2],pivot_table.iloc[4,2],pivot_table.iloc[5,2],pivot_table.iloc[6,2],pivot_table.iloc[7,2])),
        ('证券公司调整各级干部%d人，其中：' %zq_total),
        ('总部、分（子）公司以上干部调整%d人（包括引进%d人、提聘%d人、平调%d人、降职%d人、免职%d人、离职%d人、兼职%d人、免兼职%d人）；' %(zqzb_sum.iloc[8],zqzb_sum.iloc[0],zqzb_sum.iloc[1],zqzb_sum.iloc[2],zqzb_sum.iloc[3],zqzb_sum.iloc[4],zqzb_sum.iloc[5],zqzb_sum.iloc[6],zqzb_sum.iloc[7])),
        ('营业部干部调整%d人。（包括引进%d人、提聘%d人、平调%d人、降职%d人、免职%d人、离职%d人、兼职%d人、免兼职%d人）；' %(yyb_sum.iloc[8],yyb_sum.iloc[0],yyb_sum.iloc[1],yyb_sum.iloc[2],yyb_sum.iloc[3],yyb_sum.iloc[4],yyb_sum.iloc[5],yyb_sum.iloc[6],yyb_sum.iloc[7])),
        ('%s调整%d人。（包括引进%d人、提聘%d人、平调%d人、降职%d人、免职%d人、离职%d人、兼职%d人、免兼职%d人）。' %(pivot_table.columns[8],pivot_table.iloc[8,8],pivot_table.iloc[0,8],pivot_table.iloc[1,8],pivot_table.iloc[2,8],pivot_table.iloc[3,8],pivot_table.iloc[4,8],pivot_table.iloc[5,8],pivot_table.iloc[6,8],pivot_table.iloc[7,8])),
        (''),
        ('二、本年度%s干部%d人，其中总部级干部%d人。%s的干部中，35岁及以下的干部%d人，占比%.2f%%。' %(pivot_table.index[0],pivot_table.iloc[0,9],jtzqzb_sum['引进'],pivot_table.index[0],yj_35.shape[0],(100*yj_35.shape[0]/yj_all.shape[0]))),
        ('本年度%s干部%d人，其中总部级干部%d人。%s的干部中，35岁及以下的干部%d人，占比%.2f%%。' %(pivot_table.index[1],pivot_table.iloc[1,9],jtzqzb_sum['提聘'],pivot_table.index[1],tp_35.shape[0],(100*tp_35.shape[0]/tp_all.shape[0]))),
        (''),
        ('三、经营管理业绩不佳、担当作为不力的%d名总部级干部、%d名营业部干部、%d名二级部门经理进行了免职；%d名总部级干部、%d名营业部干部、%d名二级部门经理进行了降级。（还需另行统计因业绩承诺未完成，仅降职等不变动职务的）' %(mz_yj_zb.shape[0],mz_yj_yyb.shape[0],mz_yj_bmjl.shape[0],jj_yj_zb.shape[0],jj_yj_yyb.shape[0],jj_yj_bmjl.shape[0])),
        ('因违纪原因对%d名总部级干部、%d名营业部干部、%d名二级部门经理进行了免职；%d名总部级干部、%d名营业部干部、%d名二级部门经理进行了降级。' %(mz_jw_zb.shape[0],mz_jw_yyb.shape[0],mz_jw_bmjl.shape[0],jj_jw_zb.shape[0],jj_jw_yyb.shape[0],jj_jw_bmjl.shape[0]))]

text_output = pd.DataFrame(text)

pt_output = pd.ExcelWriter(r'E:\1-统计\%s\raw\年度干部变动统计-截止%sraw.xlsx' %(date,date))
data.to_excel(pt_output, sheet_name='干部变动明细', index=False)
pivot_table.to_excel(pt_output, sheet_name='透视图')
pivot_table2.to_excel(pt_output, sheet_name='透视图2')
text_output.to_excel(pt_output, sheet_name='文字描述', index=False)
yj_all.to_excel(pt_output, sheet_name='中间表-引进', index=False)
yj_35.to_excel(pt_output, sheet_name='中间表-引进35岁', index=False)
tp_all.to_excel(pt_output, sheet_name='中间表-提聘', index=False)
tp_35.to_excel(pt_output, sheet_name='中间表-提聘35岁', index=False)
pt_output.save()

pt_output2 = pd.ExcelWriter(r'E:\1-统计\%s\raw\年度干部变动统计-免职降职名单.xlsx' %date)
mz_yj.to_excel(pt_output2, sheet_name='业绩原因免职', index=False)
jj_yj.to_excel(pt_output2, sheet_name='业绩原因降职', index=False)
mz_jw.to_excel(pt_output2, sheet_name='违纪原因免职', index=False)
jj_jw.to_excel(pt_output2, sheet_name='违纪原因降职', index=False)
pt_output2.save()
