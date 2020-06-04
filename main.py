# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:30:44 2020

@author: aelksnis
"""
import tkinter as tk

def createMainClassesWindow():
    #space_between_lbl_and_txt = 
    window = tk.Tk()
    
    # Name of the item class
    lblName = tk.Label(window, text="Class name", fg="black", font=("Arial", 10), width="10")
    lblName.grid(row=0, column=0)
    txtName = tk.Text(window, height=1, width=30)
    #txtName.insert(tk.END, "Class name")
    txtName.grid(row=0, column=1)

    # Description of the item class
    lblDescr = tk.Label(window, text="Class description", fg="black", font=("Arial", 10))
    lblDescr.grid(row=1, column=0)
    txtDescr = tk.Text(window, height=1, width=30)
    txtDescr.grid(row=1, column=1)
    
    # add title
    window.title("Check Out Data Entry - Main Classes")
    
    # set frame and geometry (width x height + XPOS + YPOS)
    window.geometry("500x500+100+200")
    
    window.mainloop()
    
    
if __name__ == '__main__':
    createMainClassesWindow()