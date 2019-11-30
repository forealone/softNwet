# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:05:27 2019

@author: asus
"""

#canvas

import tkinter as tk

window = tk.Tk()

window.title('My Window')

window.geometry('1024x768')

canvas = tk.Canvas(window, bg='green', height=500, width=500)

image_file = tk.PhotoImage(file='pikachu.gif')

image = canvas.create_image(250, 0, anchor='n', image=image_file)  # 图片锚定点（图片顶端的中间点位置）放在画布（250,0）坐标处

# 定义多边形参数，然后在画布上画出指定图形
x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)  #画直线
oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')  #画圈
arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)  #画扇型，从0度到180度
rect = canvas.create_rectangle(330, 30, 330+20, 30+20)  #画矩形
canvas.pack()


def moveit():
    canvas.move(rect, 2, 2)  #移动图形，步长2,2


b = tk.Button(window, text='move item', command=moveit).pack()

window.mainloop()
