# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 09:47:35 2021

@author: User
"""
from tkinter import Toplevel
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Tk
from tkinter import StringVar
from tkinter import messagebox

class PopUp(Toplevel):
    def __init__(self, value):
        Toplevel.__init__(self)
        
        self.value = StringVar()
        
        label = Label(self, text='receiver\'s name')
        label.pack()
        
        entry = Entry(self, textvariable=self.value)
        entry.pack()
        
        button = Button(self, text='enter', command=lambda:self.callback(value))
        button.pack()
    #所有操作在这个函数中完成
    def callback(self, value):
        value.append(self.value.get())  #将self.value的值传递给Gui，用list而不是string
        self.destroy()
        
        
class Gui():
    def __init__(self, root):
        self.root = root
        self.root.geometry('100x100')
        
        self.value = []
        
        button_1 = Button(root, text='pop_up', bg='yellow', command=lambda:self.callback_1())
        button_1.pack(expand='yes')
        
        button_2 = Button(root, text='show', bg='green', command=lambda:self.callback_2())
        button_2.pack(expand='yes')

    def callback_1(self):
        PopUp(self.value)

    def callback_2(self):
        messagebox.showinfo(message='value : %s' % str(self.value))
         
         
root = Tk()
gui= Gui(root)
root.mainloop()