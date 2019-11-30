# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:56:55 2019

@author: asus
"""

#checkbutton

import tkinter as tk

window = tk.Tk()

window.geometry('500x300')

window.title('My Window')

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()

def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python ')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='I do not love either')
    else:
        l.config(text='I love both')
        
#定义两个Checkbutton部件，传值原理类似于radiobutton
c1 = tk.Checkbutton(window, text='python', variable=var1, onvalue=1, offvalue=0, command=print_selection)
c1.pack()
c2 = tk.Checkbutton(window, text='C++', variable=var2, onvalue=1, offvalue=0, command=print_selection)
c2.pack()

window.mainloop()
