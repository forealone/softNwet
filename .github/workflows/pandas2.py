# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 16:38:14 2019

@author: User
"""
input('即将开始制作月报-本年度干部变动统计，按回车键继续...')

import pandas as pd
print('\n 读取：E:\\组织部共享\\干部结构统计表\\本年度干部变动统计-模板.xlsx')
input('确保当月干部变动已汇总进“本年度干部变动统计-模板.xlsx”，按回车键继续...')
data_io = pd.io.excel.ExcelFile(r'E:\组织部共享\干部结构统计表\本年度干部变动统计-模板.xlsx')
data = pd.read_excel(data_io,sheet_name='干部变动统计')
data_io.close()
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
pivot_table = pd.pivot_table(data,index=['调整类别'],columns=['干部类别'], values=['姓名'], aggfunc={'姓名':'count'}, dropna=True, fill_value=0, margins=True, margins_name='合计') #去除columns中为空数据、用0填充空数字、展示汇总数all
pivot_table.columns = pivot_table.columns.droplevel(level=0) 
row = ['引进','提聘','平调','降级','免职','辞职','兼职','免兼职','合计']
pivot_table = pivot_table.reindex(row)  #行索引排序（干部类型）
col = ['公司领导','集团干部','总部干部','分公司干部','子公司干部','营业部正职','营业部副职/卫星','二级部门经理','合计']
pivot_table = pivot_table.reindex(columns=col)  #列索引排序
pivot_table.fillna(0, inplace=True)

#证券公司总部分子公司干部变动人数加总
zb_sum = pivot_table.iloc[:,2] + pivot_table.iloc[:,3] + pivot_table.iloc[:,4]
zb_sum['引进']
zb_sum.iloc[8]

#营业部干部变动人数加总
yyb_sum = pivot_table.iloc[:,5] + pivot_table.iloc[:,6]

#证券公司整体变动人数加总
zq_total = pivot_table.iloc[8,2] + pivot_table.iloc[8,3] + pivot_table.iloc[8,4] + pivot_table.iloc[8,5] + pivot_table.iloc[8,6] + pivot_table.iloc[8,7]

#集团和证券公司整体变动人数加总
jtzq_total = pivot_table.iloc[8,1] + zq_total

#生成一段文字描述
text = [('2019年以来至本月底，共调整干部%s人。' %jtzq_total),
        ('%s调整干部%s人。（包括引进%s人、提聘%s人、平调%s人、降职%s人、免职%s人、离职%s人、兼职%s人、免兼职%s人）。' %(pivot_table.columns[1],pivot_table.iloc[8,1],pivot_table.iloc[0,1],pivot_table.iloc[1,1],pivot_table.iloc[2,1],pivot_table.iloc[3,1],pivot_table.iloc[4,1],pivot_table.iloc[5,1],pivot_table.iloc[6,1],pivot_table.iloc[7,1])),
        ('证券公司调整各级干部%s人，其中：' %zq_total),
        ('总部、分（子）公司以上干部调整%s人（包括引进%s人、提聘%s人、平调%s人、降职%s人、免职%s人、离职%s人、兼职%s人、免兼职%s人）；' %(zb_sum.iloc[8],zb_sum.iloc[0],zb_sum.iloc[1],zb_sum.iloc[2],zb_sum.iloc[3],zb_sum.iloc[4],zb_sum.iloc[5],zb_sum.iloc[6],zb_sum.iloc[7])),
        ('营业部干部调整%s人。（包括引进%s人、提聘%s人、平调%s人、降职%s人、免职%s人、离职%s人、兼职%s人、免兼职%s人）；' %(yyb_sum.iloc[8],yyb_sum.iloc[0],yyb_sum.iloc[1],yyb_sum.iloc[2],yyb_sum.iloc[3],yyb_sum.iloc[4],yyb_sum.iloc[5],yyb_sum.iloc[6],yyb_sum.iloc[7])),
        ('%s调整%s人。（包括引进%s人、提聘%s人、平调%s人、降职%s人、免职%s人、离职%s人、兼职%s人、免兼职%s人）。' %(pivot_table.columns[7],pivot_table.iloc[8,7],pivot_table.iloc[0,7],pivot_table.iloc[1,7],pivot_table.iloc[2,7],pivot_table.iloc[3,7],pivot_table.iloc[4,7],pivot_table.iloc[5,7],pivot_table.iloc[6,7],pivot_table.iloc[7,7]))]
text_output = pd.DataFrame(text)

date = input('输入月度统计表的统计年月，用于命名导出文件，(格式：YYYYMM):')
print('E:\\1-统计\\%s\\raw\\' %date)
input('将输出文件至上述目录，按回车键继续...')

pt_output = pd.ExcelWriter(r'E:\1-统计\%s\raw\本年度干部变动统计-截止本月.xlsx' %date)
data.to_excel(pt_output, sheet_name='干部变动明细', index=False)
pivot_table.to_excel(pt_output, sheet_name='透视图')
text_output.to_excel(pt_output, sheet_name='文字描述', index=False)
pt_output.save()
