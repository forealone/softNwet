# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:37:53 2019

@author: User
"""
input('即将开始导入近两年考核结果，并做数据处理。请按回车键，并稍作等待...')

import pandas as pd  #pandas数据处理模块，pd是别名
#import sys

#导入原始数据：考核结果
eva_2018 = pd.read_excel(r'E:\2-年度考核\历年考核结果\2018考核结果汇总.xlsx',sheet_name='干部员工')
eva_2019 = pd.read_excel(r'E:\2-年度考核\历年考核结果\2019考核结果汇总.xlsx',sheet_name='干部员工')

#编辑原始数据
del eva_2018['职务']
del eva_2019['职务']
del eva_2018['序号']
del eva_2019['序号']
eva_2018['考核年度'] = None
eva_2018.loc[eva_2018[eva_2018['考核方案'].str.contains('2018')].index,['考核年度']] = '2018'
eva_2019['考核年度'] = None
eva_2019.loc[eva_2019[eva_2019['考核方案'].str.contains('2019')].index,['考核年度']] = '2019'

#输入
name = input('输入需查询的人员姓名，多个人用空格分隔：')
name_split = name.split(' ')
print(name_split ,'\n 共',len(name_split),'人')

#创建模板
somebody_eva_template = pd.DataFrame({'考核对象编码':['000000'],'考核对象':['张三'],'部门':['人力资源总部'],'考核结果':['A（优秀）'],'考核方案':['201X年干部考核方案'],'考核年度':['201X']})

#不用while循环的考核结果查询方式
somebody_2018 = eva_2018[eva_2018['考核对象'].isin(name_split)]  
somebody_2019 = eva_2019[eva_2019['考核对象'].isin(name_split)]  
somebody_eva = somebody_eva_template.append(somebody_2018,ignore_index=True)
somebody_eva = somebody_eva.append(somebody_2019,ignore_index=True)
somebody_eva.drop([0,0],inplace=True)
somebody_eva = somebody_eva.sort_values(by=['考核对象编码','考核年度'] , ascending=(True,True))
somebody_eva = somebody_eva.reset_index(drop=True)

'''
i = 0
while i < len(name_split) :
    somebody_2017 = eva_2017[eva_2017['考核对象']==name_split[i]]
    somebody_2018 = eva_2018[eva_2018['考核对象']==name_split[i]]
    somebody_eva_template = somebody_eva_template.append(somebody_2017,ignore_index=True)
    somebody_eva_template = somebody_eva_template.append(somebody_2018,ignore_index=True)    
    i=i+1
else:
    print('查询并输出 %d 人考核结果：' %(i))
    somebody_eva = somebody_eva_template
    somebody_eva.drop([0,0],inplace=True)
    print(somebody_eva)
    #somebody_eva_template.drop(['考核对象编码','考核对象','部门','考核结果','考核方案'],axis=1,inplace=True)
'''

#查重名
if len(somebody_eva['考核对象'].drop_duplicates()) == len(somebody_eva['考核对象编码'].drop_duplicates()):
    pass
else:
    print('可能存在重名人员 %d 人，请注意检查' %(len(somebody_eva['考核对象编码'].drop_duplicates())-len(somebody_eva['考核对象'].drop_duplicates())))

#格式调整
somebody_eva2 = somebody_eva.groupby(['考核对象编码','考核对象','考核年度','部门','考核结果'])['考核对象编码'].count()
print(somebody_eva2)

#保存
somebody_eva_output = pd.ExcelWriter(r'C:\Users\User\Desktop\临时查询考核结果.xlsx')
somebody_eva.to_excel(somebody_eva_output,sheet_name='格式1')
somebody_eva2.to_excel(somebody_eva_output,sheet_name='格式2')
somebody_eva_output.save()

input('考核结果保存至桌面，按回车键关闭窗口')

'''
#合并同类项
def ab(df):
    return','.join(somebody_eva.values)
    
somebody_eva = somebody_eva.groupby(['考核对象编码','考核对象'])['考核结果'].apply(ab)
somebody_eva = somebody_eva.reset_index()
somebody_eva
'''
