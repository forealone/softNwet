# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 13:07:24 2019

@author: asus
"""


import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()

window.title('My Window')

window.geometry('800x600')

#创建主frame到主window窗口
frame = tk.Frame(window)
frame.pack()

#创建第二层frame，到主frame上
frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')

img = Image.open('King.jpg')

photo = ImageTk.PhotoImage(img)

b1_canvas = tk.Canvas(frame_l, bg='green', height=192, width=139)
b2_canvas = tk.Canvas(frame_r, bg='green', height=192, width=139)
test1_canvas = tk.Canvas(window, bg='green', height=192, width=139)
test2_canvas = tk.Canvas(window, bg='green', height=192, width=139)
test3_canvas = tk.Canvas(window, bg='green', height=192, width=139)
test4_canvas = tk.Canvas(window, bg='green', height=192, width=139)

image = b1_canvas.create_image(142, 0, anchor='ne', image=photo)  
image = b2_canvas.create_image(142, 0, anchor='ne', image=photo)  
image = test1_canvas.create_image(142, 0, anchor='ne', image=photo)  
image = test2_canvas.create_image(142, 0, anchor='ne', image=photo)  
image = test3_canvas.create_image(142, 0, anchor='ne', image=photo)  
image = test4_canvas.create_image(142, 0, anchor='ne', image=photo)  

b1_canvas.pack()
b2_canvas.pack()
test1_canvas.pack(side='left')
test2_canvas.pack(side='left')
test3_canvas.pack(side='right')
test4_canvas.pack(side='right')

window.mainloop()
