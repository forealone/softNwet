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

img = Image.open('King.jpg')

photo = ImageTk.PhotoImage(img)

canvas = tk.Canvas(window, bg='green', height=192, width=139)

image = canvas.create_image(142, 0, anchor='ne', image=photo)  # 图片锚定点（图片顶端的中间点位置）放在画布（250,0）坐标处

canvas.pack()

window.mainloop()
