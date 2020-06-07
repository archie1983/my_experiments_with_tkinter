# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:28:35 2020

@author: aelksnis
"""
import tkinter as tk
import AddSalesItems as asi
import SalesItem as si
from functools import partial

class AddClass:

    def __init__(self):
        self.window = tk.Tk()

        # variables holding the input values
        self.txt_name_val = tk.StringVar()
        self.txt_descr_val = tk.StringVar()
    
        # number of entries added
        self.number_of_entries = 0
        self.top_classes = []
    
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
    
        frmButtons = tk.Frame(self.window)
        frmButtons.grid(row=3, column=0, columnspan=2)
        # Buttons for quitting and adding the new class
        btnAddClass = tk.Button(frmButtons,
                           text="Add Class",
                           command=self.add_class)
        btnAddClass.grid(row=0, column=0)
        
        btnQuit = tk.Button(frmButtons, 
                           text="QUIT", 
                           fg="red",
                           command=self.window.destroy)
        btnQuit.grid(row=0, column=1)
        
        btnAddItems = tk.Button(frmButtons, 
                           text="Add Sales Items", 
                           fg="blue",
                           command=self.open_sales_items_window)
        btnAddItems.grid(row=0, column=2)
        
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
    
    # Adds the class item to the main list and displays it in the scroller
    # form.
    def add_class(self):
        class_name = self.txt_name_val.get()
        class_descr = self.txt_descr_val.get()
        
        if class_name == "":
            return

        self.top_classes.append(si.SalesItem(self.number_of_entries + 1, class_name, class_descr))
        
        self.add_all_items_to_scroller()
        
        self.number_of_entries += 1
        
        self.txt_name_val.set("")
        self.txt_descr_val.set("")
        
    # deletes class identified by its ID
    def delete_item(self, class_id):
        new_class_list = []
        for item in self.top_classes:
            if item.si_id != class_id:
                new_class_list.append(item)
            
        self.top_classes = new_class_list
        
        self.add_all_items_to_scroller()

    # Adds all items to the scroller to be seen and be able to pick for
    # editing or deleteing.
    def add_all_items_to_scroller(self):
        # First clearing the frame
        for widget in self.frmClasses.winfo_children():
            widget.destroy()
        
        # Now adding the items from the collection
        row_counter = 0
        for item in self.top_classes:
            self.add_item_row_to_scroller(row_counter, item)
            row_counter += 1

    # Add a single row of the items to the scroller
    # This needs to be used while iterating through all items.
    def add_item_row_to_scroller(self, row_counter, item):
        lblID = tk.Label(self.frmClasses, text=item.si_id, fg="blue", font=("Arial", 10))
        lblID.grid(row=row_counter, column=0)
        
        lblName = tk.Label(self.frmClasses, text=item.name, fg="blue", font=("Arial", 10))
        lblName.grid(row=row_counter, column=1)
        
        lblDescr = tk.Label(self.frmClasses, text=item.descr, fg="blue", font=("Arial", 10))
        lblDescr.grid(row=row_counter, column=2)

        # Delete button        
        delete_action = partial(self.delete_item, item.si_id)
        btnDelete = tk.Button(self.frmClasses, text="Delete", command=delete_action)
        btnDelete.grid(row=row_counter, column=3)
    
    # Opens the window that lets adding sales items with the entered classes
    # choosable parents.
    def open_sales_items_window(self):
        # current window needs to close first, because in the 
        # "createSalesItemInputWindow" we'll call self.window.mainloop()
        # which will not return for some time.
        self.window.destroy()
        si_win = asi.AddSalesItems(self.top_classes)
        si_win.createSalesItemInputWindow()