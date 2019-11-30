# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:49:41 2019

@author: asus
"""

#frame

import tkinter as tk

window = tk.Tk()

window.title('My Window')

window.geometry('500x300')

tk.Label(window, text='on the window', bg='red', font=('Arial', 16)).pack()

#创建主frame到主window窗口
frame = tk.Frame(window)
frame.pack()

#创建第二层frame，到主frame上
frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')

tk.Label(frame_l,text='on the frame_l1', bg='green').pack()
tk.Label(frame_l,text='on the frame_l2', bg='green').pack()
tk.Label(frame_l,text='on the frame_l3', bg='green').pack()
tk.Label(frame_r,text='on the frame_r1', bg='yellow').pack()
tk.Label(frame_r,text='on the frame_r2', bg='yellow').pack()
tk.Label(frame_r,text='on the frame_r3', bg='yellow').pack()

window.mainloop()
