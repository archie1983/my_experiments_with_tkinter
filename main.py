# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:30:44 2020

@author: aelksnis
"""
import tkinter as tk

def createMainClassesWindow():
    row_top_spacing = 27
    row_top = 10
    row_left = 10
    #space_between_lbl_and_txt = 
    window = tk.Tk()
    
    # Name of the item class
    lblName = tk.Label(window, text="Class name", fg="black", font=("Arial", 10), width="10")
    lblName.place(x=row_left, y=row_top)
    txtName = tk.Text(window, height=1, width=30)
    #txtName.insert(tk.END, "Class name")
    txtName.place(x=100, y=row_top)
    row_top += row_top_spacing

    # Description of the item class
    lblDescr = tk.Label(window, text="Class description", fg="black", font=("Arial", 10))
    lblDescr.place(x=row_left, y=row_top)
    txtDescr = tk.Text(window, height=1, width=30)
    txtDescr.place(x=100, y=row_top)
    row_top += row_top_spacing
    
    # add title
    window.title("Check Out Data Entry - Main Classes")
    
    # set frame and geometry (width x height + XPOS + YPOS)
    window.geometry("500x500+100+200")
    
    window.mainloop()
    
    
if __name__ == '__main__':
    createMainClassesWindow()