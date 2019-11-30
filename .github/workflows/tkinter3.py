# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:39:34 2019

@author: asus
"""

#radiobutton

import tkinter as tk

window = tk.Tk()

window.geometry('500x300')

var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

#定义选项触发函数功能
def print_selection():
    l.config(text='you have selected ' + var.get())

#创建三个radiobutton选项，其中variable=var, value='A'的意思就是，当我们鼠标选中了其中一个选项，把value的值A放到变量var中，然后赋值给variable
r1 = tk.Radiobutton(window, text='Option A', variable=var, value='A', command=print_selection)
r1.pack()
r2 = tk.Radiobutton(window, text='Option B', variable=var, value='B', command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='Option C', variable=var, value='C', command=print_selection)
r3.pack()

window.mainloop()
