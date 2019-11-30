# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Label,Button,Entry,Text

import tkinter as tk

window = tk.Tk()  #实例化object，建立窗口window

window.title('My Window')

window.geometry('500x300')  #这里的乘是小x

var = tk.StringVar()   #将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l2 = tk.Label(window, textvariable=var, bg='green' , fg='white' , font=('Arial',12),width=30 , height=2)
l2.pack()
l = tk.Label(window, text='this is Tkinter', bg='green', font=('Arial',12),width=30, height=2)
l.pack()

#定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False
def hit_me():  
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')
        
b = tk.Button(window,text='hit me', font=('Arial',12), width=10,height=1, command=hit_me)
b.pack()

e = tk.Entry(window, show=None, font=('Arial',14))  #show='*'可显示为密文形式
e.pack()

#定义两个触发事件时的函数insert_point和insert_end（注意：因为Python的执行顺序是从上往下，所以函数一定要放在按钮的上面）
def insert_point():  # 在鼠标焦点处插入输入内容
    var2 = e.get()
    t.insert('insert', var2)
def insert_end():  # 在文本框内容最后接着插入输入内容
    var2 = e.get()
    t.insert('end', var2)
    
#创建并放置两个按钮分别触发两种情况
b1 = tk.Button(window, text='insert point', width=10, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(window,text='insert end', width=10, height=2, command=insert_end)
b2.pack()

t = tk.Text(window, height=3)
t.pack()

#主窗口循环显示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
