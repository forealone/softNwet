# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:07:55 2019

@author: asus
"""

#scale

import tkinter as tk

window = tk.Tk()

window.title('My Window')

window.geometry('500x300')

l = tk.Label(window, bg='green', fg='white', width=20, text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected ' + v)


#创建一个尺度滑条，长度200字符，从0开始10结束，以2为刻度，精度为0.01，触发调用print_selection函数
s = tk.Scale(window, label='try me', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0, tickinterval=2, resolution=0.01, command=print_selection)
s.pack()

window.mainloop()

