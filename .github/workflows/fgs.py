# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:39:37 2020

@author: User
"""
import pandas as pd

#定义分级和编制，根据实际情况更新
grade0 = pd.DataFrame({'0':['上海分公司','一级'],'1':['杭州分公司','二级'],'2':['江苏分公司','二级'],'3':['四川分公司','三级'],'4':['北京分公司','三级'],
                       '5':['深圳分公司','三级'],'6':['湖北分公司','三级'],'7':['广东分公司','三级'],'8':['温州分公司','三级'],'9':['厦门分公司','三级'],
                       '10':['辽宁分公司','四级'],'11':['江西分公司','四级'],'12':['重庆分公司','四级'],'13':['大连分公司','四级'],'14':['宁波分公司','四级'],
                       '15':['广西分公司','四级'],'16':['湖南分公司','四级'],'17':['天津分公司','四级'],'18':['山东分公司','四级'],'19':['吉林分公司','四级'],
                       '20':['安徽分公司','四级'],'21':['海南分公司','五级'],'22':['福建分公司','五级'],'23':['甘肃分公司','五级'],'24':['河南分公司','五级'],
                       '25':['黑龙江分公司','五级'],'26':['陕西分公司','五级'],'27':['贵州分公司','五级'],'28':['青岛分公司','五级'],'29':['河北分公司','五级'],
                       '30':['内蒙古分公司','五级'],'31':['山西分公司','五级'],'32':['云南分公司','五级'],'33':['宁夏分公司','五级'],'34':['西部证券','一级'],
                       '35':['上海第二分公司','未定级'],'36':['上海自贸区分公司','未定级']})
grade0 = pd.DataFrame(grade0.values.T, index=grade0.columns, columns=['部门名称','分公司评级'])
grade1 = pd.DataFrame({'分公司评级':['一级','二级','三级','四级','五级','未定级'], '编制':['一正四副','一正三副','一正二副','一正二副','一正一副','-']})
grade2 = pd.DataFrame({'编制':['一正四副','一正三副','一正二副','一正一副','-'], '编制数':[5,4,3,2,'-']})

date = input('输入月度统计表的年月，(格式：YYYYMM):')
print('\n E:\\1-统计\\%s\\raw\\' %date)
input('请检查文件目录是否正确，确保目录下有以下文件：\n “干部信息明细表（数据清洗）.xlsx” \n 按回车键继续... \n')
cadre_data = pd.read_excel(r'E:\1-统计\%s\raw\干部信息明细表（数据清洗）.xlsx' %date,sheet_name='干部信息明细表总表')

cadre_data_fgs = cadre_data[cadre_data['干部类型'].isin(['分公司正职','分公司副职','分公司助理'])]

#分公司干部中，四川分公司李强、自贸区分公司徐颖系兼职，另行添加至名单中。如有调整需修改代码
cadre_liqiang = cadre_data[cadre_data['工号'] == '006598']
cadre_liqiang.loc[cadre_liqiang[cadre_liqiang['工号']=='006598'].index,['组织','一级部门','部门名称','职务','本岗位任职日期']] = ['申万宏源证券有限公司四川分公司','四川分公司','四川分公司','副总经理（兼）','2018-01-05']

cadre_xuying = cadre_data[cadre_data['工号'] == '002069']
cadre_xuying.loc[cadre_xuying[cadre_xuying['工号']=='002069'].index,['组织','一级部门','部门名称','职务','本岗位任职日期']] = ['申万宏源证券有限公司上海分公司','上海自贸区分公司','上海自贸区分公司','总经理（兼）','2020-06-01']

cadre_data_fgs = pd.concat([cadre_data_fgs,cadre_liqiang,cadre_xuying], axis=0, ignore_index=False, sort=False)

cadre_data_fgs = cadre_data_fgs.reset_index(drop=True)

cadre_data_fgs.loc[cadre_data_fgs[cadre_data_fgs['工号']=='360001'].index,['一级部门','部门名称']] = ['甘肃分公司','甘肃分公司']

#刚引进的干部当月工资职等查不出来为空，会导致groupby时丢失数据，故需fillna
cadre_data_fgs['职等'].fillna('-',inplace=True)

del cadre_data_fgs['组织']
del cadre_data_fgs['身份证号']
del cadre_data_fgs['政治面貌分类']
del cadre_data_fgs['最高学历分类']
del cadre_data_fgs['年龄段']
del cadre_data_fgs['出生年份']
del cadre_data_fgs['退岗标识']
del cadre_data_fgs['退休标识']
del cadre_data_fgs['基准年份']
del cadre_data_fgs['2018年度考核结果']
del cadre_data_fgs['2019年度考核结果']
del cadre_data_fgs['考核结果是否符合提聘条件']
del cadre_data_fgs['总部级干部类别']
del cadre_data_fgs['部门类别']
del cadre_data_fgs['公司领导类别1']
del cadre_data_fgs['公司领导类别2']

cadre_data_fgs = pd.merge(cadre_data_fgs,grade0,on='部门名称',how='left')
cadre_data_fgs = pd.merge(cadre_data_fgs,grade1,on='分公司评级',how='left')
cadre_data_fgs = pd.merge(cadre_data_fgs,grade2,on='编制',how='left')

cadre_data_fgs.groupby(['部门名称'])['年龄'].describe().unstack()
cadre_data_fgs_count = cadre_data_fgs.groupby(['部门名称','分公司评级'])['工号'].count()
cadre_data_fgs_count.iloc[0]
cadre_data_fgs_groupby = cadre_data_fgs.groupby(['分公司评级','编制','编制数','部门名称','工号','人员姓名','性别','职务','干部类型','干部职级','政治面貌','最高学历','出生日期','年龄','职等','本岗位任职日期','现职级任职日期'])['工号'].count()


cadre_data_output = pd.ExcelWriter(r'E:\1-统计\%s\raw\缺编表test.xlsx' %date)
cadre_data_fgs.to_excel(cadre_data_output, sheet_name='分公司缺编情况1', index=False)
cadre_data_fgs_groupby.to_excel(cadre_data_output, sheet_name='分公司缺编情况2')
cadre_data_output.save()

