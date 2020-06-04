# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:30:44 2020

@author: aelksnis
"""
from tkinter import *

def createWindow():
    window = Tk()
    
    # add widgets here
    
    lbl = Label(window, text="Check Out Data Entry", fg="blue", font=("Arial", 17))
    lbl.place(x=100, y=100)
    
    # add title
    window.title("Check Out Data Entry")
    
    # set frame and geometry (width x height + XPOS + YPOS)
    window.geometry("500x500+100+200")
    
    window.mainloop()
    
    
if __name__ == '__main__':
    createWindow()