# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:30:44 2020

@author: aelksnis
"""
import tkinter as tk

window = tk.Tk()
txt_name_val = tk.StringVar()
txt_descr_val = tk.StringVar()

def createMainClassesWindow():    
    # Name of the item class
    lblName = tk.Label(window, text="Class name", fg="black", font=("Arial", 10), width="10")
    lblName.grid(row=0, column=0)
    txtName = tk.Entry(window, width=30, textvariable=txt_name_val)
    #txtName.insert(tk.END, "Class name")
    txtName.grid(row=0, column=1)

    # Description of the item class
    lblDescr = tk.Label(window, text="Class description", fg="black", font=("Arial", 10))
    lblDescr.grid(row=1, column=0)
    txtDescr = tk.Entry(window, width=30, textvariable=txt_descr_val)
    txtDescr.grid(row=1, column=1)

    btnAddClass = tk.Button(window,
                       text="Add Class",
                       command=add_class)
    btnAddClass.grid(row=2, column=0)
    
    button = tk.Button(window, 
                       text="QUIT", 
                       fg="red",
                       command=window.destroy)
    button.grid(row=2, column=1)
    
    # add title
    window.title("Check Out Data Entry - Main Classes")
    
    # set frame and geometry (width x height + XPOS + YPOS)
    window.geometry("500x500+100+200")
    
    window.mainloop()
    
def add_class():
    txt_name_val.set("AAAAA")
    txt_descr_val.set("BBBB")

if __name__ == '__main__':
    createMainClassesWindow()