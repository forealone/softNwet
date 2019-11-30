# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:33:40 2019

@author: asus
"""

#grid/pack/place

'''
The Grid Geometry Manager
http://effbot.org/tkinterbook/grid.htm

The Pack Geometry Manager
http://effbot.org/tkinterbook/pack.htm

The Place Geometry Manager
http://effbot.org/tkinterbook/place.htm
'''

import tkinter as tk
 
window = tk.Tk()
 
window.title('My Window')
 
window.geometry('500x300')  
'''
# grid 放置方法
for i in range(3):
    for j in range(3):
        tk.Label(window, text=('%s,%s' %(i,j))).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)  #参数 row 为行，colum 为列，padx 就是单元格左右间距，pady 就是单元格上下间距，ipadx是单元格内部元素与单元格的左右间距，ipady是单元格内部元素与单元格的上下间距。

# pack 放置方法
tk.Label(window, text='P', fg='red').pack(side='top')    # 上
tk.Label(window, text='P', fg='green').pack(side='bottom') # 下
tk.Label(window, text='P', fg='yellow').pack(side='left')   # 左
tk.Label(window, text='P', fg='blue').pack(side='right')  # 右
'''
# place 放置方法（精准的放置到指定坐标点的位置上）
tk.Label(window, text='Pl', font=('Arial', 20), ).place(x=50, y=100, anchor='nw')

window.mainloop()