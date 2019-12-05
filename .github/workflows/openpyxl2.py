# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 08:59:33 2019

@author: User
"""

input('即将对集团和证券公司干部信息明细表进行格式美化，按回车键继续...')

from openpyxl import load_workbook
from openpyxl.styles import Font, NamedStyle
from openpyxl.styles import PatternFill, Border, Side, Alignment

date = input('输入月度统计表的年月，(格式：YYYYMM):')
print('E:\\1-统计\\%s\\raw\\ \n' %date)
input('请检查文件目录是否正确，确保目录下有以下文件：\n 干部信息明细表（编辑）.xlsx \n 按回车键继续...')

wb = load_workbook(r'E:\1-统计\%s\raw\干部信息明细表（编辑）.xlsx' %date)

ws = wb['干部信息明细表']

#字体
font1 = Font(name='宋体', color='000000', size=10, b=True)
font2 = Font(name='宋体', color='000000', size=10)

#单元格格式
ali = Alignment(horizontal='center', vertical='center',wrap_text=True )

#颜色填充
fill1 = PatternFill('solid', fgColor='D9D9F3')
fill2 = PatternFill('solid', fgColor='FFFFFF')

#边线和边框
sd1 = Side(style='thin', color='000000')
sd2 = Side(style='medium', color='000000')
border1 = Border(top=sd1, bottom=sd2, left=sd1, right=sd1)
border2 = Border(top=sd1, bottom=sd1, left=sd1, right=sd1)

#打包以上格式
sty1 = NamedStyle(name='sty1', font=font1, fill=fill1,border=border1, alignment=ali)
sty2 = NamedStyle(name='sty2', font=font2, fill=fill2,border=border2, alignment=ali)

ws.delete_cols(18, 8) #从18列开始删除，往后删8列（删除之前用pandas匹配的用于统计汇总的数据字段）

rows = ws.max_row
cols = ws.max_column

#第一行表头和第二行开始的数据分别匹配格式
for r in range(1, rows+1):
    for c in range(1, cols+1):
        if r == 1:
            ws.cell(r, c).style = sty1
        else:
            ws.cell(r, c).style = sty2

print('E:\\1-统计\\%s\\raw\\' %date)
input('将输出文件至上述目录，按回车键继续...')
wb.save(r'E:\1-统计\%s\raw\干部信息明细表（编辑2）.xlsx' %date)