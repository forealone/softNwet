# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 13:38:29 2019

@author: User
"""

'''
import tkinter
tkinter._test()
'''

from tkinter import *
import tkinter as tk


#定义按钮1
def newlabel():
    global window
    s = tk.Label(window,text ="一行") 
    s.pack()

#定义按钮2
def newlabel2(event):
    global window
    s = tk.Label(window,text = "又一行")
    s.pack()

window = tk.Tk()

window.wm_title("修改窗口标题")

l = tk.Label(window, text="标签空间2-设置背景颜色",background = "green")
l.pack()

b1 = tk.Button(window, text="点一下新增一行",command = newlabel)
b1['width'] = 20
b1['background'] = 'red'
b1.pack()

b2 = tk.Button(window,text = "点一下新增一行（方式2）")
#b2.flash()
b2['width'] = 20
b2['height'] = 4
b2.bind("<Button-1>",newlabel2)  #<Button-1>为左键单击事件，newlabel2回调函数
b2.pack(expand=YES, fill=X, anchor=NE)

window.mainloop()

'''
#pack布局可实现的各种样式
root = Tk()
Button(root,text = 'A').pack(side=LEFT,expand=YES,fill=Y)
Button(root,text = 'B').pack(side=TOP,expand=YES,fill=BOTH)
Button(root,text = 'C').pack(side=RIGHT,expand=YES,fill=NONE,anchor=NE)
Button(root,text = 'D').pack(side=LEFT,expand=NO,fill=Y)
Button(root,text = 'E').pack(side=TOP,expand=NO,fill=BOTH)
Button(root,text = 'F').pack(side=BOTTOM,expand=YES)
Button(root,text = 'G').pack(anchor=SE)

root.mainloop()
'''

'''
#grid布局
grid_test = Tk()
Label(grid_test,text='账号：').grid(row=0,sticky=W)
Entry(grid_test).grid(row=0,column=1,sticky=E)

Label(grid_test,text='密码：').grid(row=1,sticky=W)
Entry(grid_test).grid(row=1,column=1,sticky=E)

Button(grid_test,text='登录').grid(row=2,column=1,sticky=S)
grid_test.mainloop()
'''

'''
常用事件：
<Button-1>为左键单击,<Button-2>中键，<Button-3>右键
<KeyPress-A>为A键被按下
<Control-V>为Ctrl和V键被按下
<F1>表示F1键被按下
'''


