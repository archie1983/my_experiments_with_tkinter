# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:28:35 2020

@author: aelksnis
"""
import tkinter as tk

class AddClass:

    def __init__(self):
        self.window = tk.Tk()
        
        # variables holding the input values
        self.txt_name_val = tk.StringVar()
        self.txt_descr_val = tk.StringVar()
    
        # number of entries added
        self.number_of_entries = 0
    
    def createMainClassesWindow(self):    
        # Name of the item class
        lblName = tk.Label(self.window, text="Class name", fg="black", font=("Arial", 10), width="10")
        lblName.grid(row=0, column=0)
        txtName = tk.Entry(self.window, width=30, textvariable=self.txt_name_val)
        #txtName.insert(tk.END, "Class name")
        txtName.grid(row=0, column=1)
    
        # Description of the item class
        lblDescr = tk.Label(self.window, text="Class description", fg="black", font=("Arial", 10))
        lblDescr.grid(row=1, column=0)
        txtDescr = tk.Entry(self.window, width=30, textvariable=self.txt_descr_val)
        txtDescr.grid(row=1, column=1)
    
        # Frame containing current classes
        # 1st creating a form where we'll keep a scrolling canvas
        frmScroller4Classes = tk.Frame(self.window,
            border=1,
            relief=tk.GROOVE,
            background="blue")
        frmScroller4Classes.grid(row=2, column=0, columnspan=2, sticky=tk.N+tk.S)
        
        # Creating canvas on scroller frame
        self.canvas = tk.Canvas(frmScroller4Classes)
        self.canvas.grid(row=0, column=0)
        
        # Creating scrollbar for the canvas, which will be on the same scroller frame.
        myscrollbar = tk.Scrollbar(frmScroller4Classes,orient="vertical",command=self.canvas.yview)
        myscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)
        
        # New frame for the contents on the canvas.
        
        # Frame containing current classes
        self.frmClasses = tk.Frame(self.canvas)
        self.canvas.configure(yscrollcommand=myscrollbar.set)
        self.canvas.create_window((0,0),window=self.frmClasses,anchor='nw')
        self.frmClasses.bind("<Configure>", self.onFrameConfigure)
    
        # Buttons for quitting and adding the new class
        btnAddClass = tk.Button(self.window,
                           text="Add Class",
                           command=self.add_class)
        btnAddClass.grid(row=3, column=0)
        
        button = tk.Button(self.window, 
                           text="QUIT", 
                           fg="red",
                           command=self.window.destroy)
        button.grid(row=3, column=1)
        
        # add title
        self.window.title("Check Out Data Entry - Main Classes")
        
        # set frame and geometry (width x height + XPOS + YPOS)
        self.window.geometry("500x500+100+200")
        
        self.onFrameConfigure(None)
        
        self.window.mainloop()
        
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        #self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=400,height=200)
    
    def add_class(self):
        class_name = self.txt_name_val.get()
        class_descr = self.txt_descr_val.get()
        
        if class_name == "":
            return
        
        lblID = tk.Label(self.frmClasses, text=(self.number_of_entries + 1), fg="blue", font=("Arial", 10))
        lblID.grid(row=self.number_of_entries, column=0)
        
        lblName = tk.Label(self.frmClasses, text=class_name, fg="blue", font=("Arial", 10))
        lblName.grid(row=self.number_of_entries, column=1)
        
        lblDescr = tk.Label(self.frmClasses, text=class_descr, fg="blue", font=("Arial", 10))
        lblDescr.grid(row=self.number_of_entries, column=2)
        
        self.number_of_entries += 1
        
        self.txt_name_val.set("")
        self.txt_descr_val.set("")