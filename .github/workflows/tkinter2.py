# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:54:11 2019

@author: asus
"""

#Listbox

import tkinter as tk

window = tk.Tk()

window.title('My Window')

window.geometry('500x300')

var1 = tk.StringVar()
l = tk.Label(window, bg='green', fg='yellow', font=('Arial',12), width=10, textvariable=var1)
l.pack()


var2 = tk.StringVar()
var2.set((1,2,3,4))

lb = tk.Listbox(window, listvariable=var2)

def print_selection():
    value = lb.get(lb.curselection())  #获取当前选中的文本
    var1.set(value)

b1 = tk.Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()

#创建一个list并将值循环添加到Listbox控件中
list_items = [11,22,33,44]
for item in list_items:
    lb.insert('end', item)  #从最后一个位置开始加入值
lb.insert(1,'first')  #在第一个位置加入'first'字符
lb.insert(2,'second')  #在第二个位置加入'second'字符
lb.delete(2)  #删除第二个位置的字符
lb.pack()

window.mainloop()