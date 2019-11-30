# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 22:26:28 2019

@author: asus
"""

#menu

import tkinter as tk

window = tk.Tk()

window.title('My Window')

window.geometry('500x300')
    
l = tk.Label(window,text='       ', bg='green')
l.pack()

#定义函数（菜单选项功能）
counter = 0
def do_job():
    global counter
    l.config(text='do '+ str(counter))
    counter += 1

#创建菜单栏
menubar = tk.Menu(window)
#创建菜单栏中的第一项（默认不下拉）
filemenu = tk.Menu(menubar, tearoff=0)
#将第一项命名为file，放入菜单栏
menubar.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit) #window.quit会导致程序无响应，建议导入sys库的exit

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

#创建二级菜单
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label='Import', menu=submenu, underline=0)
submenu.add_command(label='Submenu_1', command=do_job)
window.config(menu=menubar)

window.mainloop()