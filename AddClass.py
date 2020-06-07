# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:28:35 2020

Allows creating of the main classes - the items that will be used
as parents for the rest of the sales items.

@author: aelksnis
"""
import tkinter as tk
import SalesItem as si
from functools import partial

class AddClass:

    def __init__(self):
        self.window = tk.Tk()

        # variables holding the input values
        self.txt_name_val = tk.StringVar()
        self.txt_descr_val = tk.StringVar()
        
        self.add_button_name = tk.StringVar()
    
        # number of entries added
        self.number_of_entries = 0
        self.all_items = []
        
        # What we're editing - for string constants
        self.context_of_item = "Class"
        
        # ID of the item being edited if any
        self.item_id_being_edited = -1

    # Draws the main classes window
    def drawMainClassesWindow(self):
        self.frmInputs = tk.Frame(self.window)
        self.frmInputs.grid(row=0, column=0)
        
        self.row_num = 0
        # Name of the item class - this resides inside the self.frmMain
        lblName = tk.Label(self.frmInputs, text=(self.context_of_item + " name"), fg="black", font=("Arial", 10))
        lblName.grid(row=0, column=0)
        txtName = tk.Entry(self.frmInputs, width=30, textvariable=self.txt_name_val)
        txtName.grid(row=self.row_num, column=1)
        self.row_num += 1
    
        # Description of the item class - this resides inside the self.frmMain
        lblDescr = tk.Label(self.frmInputs, text=(self.context_of_item + " description"), fg="black", font=("Arial", 10))
        lblDescr.grid(row=1, column=0)
        txtDescr = tk.Entry(self.frmInputs, width=30, textvariable=self.txt_descr_val)
        txtDescr.grid(row=self.row_num, column=1)
        self.row_num += 1
    
        # Frame containing current classes
        # 1st creating a form where we'll keep a scrolling canvas
        frmScroller4Classes = tk.Frame(self.window,
            border=1,
            relief=tk.GROOVE,
            background="blue")
        frmScroller4Classes.grid(row=1, column=0, sticky=tk.N+tk.S) # this is inside self.window
        
        # Creating canvas on scroller frame
        self.canvas = tk.Canvas(frmScroller4Classes)
        self.canvas.grid(row=0, column=0) # inside frmScroller4Classes
        
        # Creating scrollbar for the canvas, which will be on the same scroller frame.
        myscrollbar = tk.Scrollbar(frmScroller4Classes,orient="vertical",command=self.canvas.yview)
        myscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)
        
        # New frame for the contents on the canvas.
        
        # Frame containing current classes
        self.frmItems = tk.Frame(self.canvas)
        self.canvas.configure(yscrollcommand=myscrollbar.set)
        self.canvas.create_window((0,0),window=self.frmItems,anchor='nw')
        self.frmItems.bind("<Configure>", self.onFrameConfigure)
    
        self.frmButtons = tk.Frame(self.window)
        self.frmButtons.grid(row=2, column=0, columnspan=2)# inside self.window
        
        # Buttons for quitting and adding the new class
        self.add_button_name.set("Add " + self.context_of_item)
        self.btnAddClass = tk.Button(self.frmButtons,
                           textvariable=self.add_button_name,
                           command=self.add_item)
        self.btnAddClass.grid(row=0, column=0)
        
        btnQuit = tk.Button(self.frmButtons, 
                           text="QUIT", 
                           fg="red",
                           command=self.window.destroy)
        btnQuit.grid(row=0, column=1)
        
        self.btnAddItems = tk.Button(self.frmButtons, 
                           text="Add Sales Items", 
                           fg="blue",
                           command=self.open_sales_items_window)
        self.btnAddItems.grid(row=0, column=2)
        
        # The header for the table holding current items
        self.setUpTableHeader()
        
        # add title
        self.window.title("Check Out Data Entry - Main Classes")
        
        # set frame and geometry (width x height + XPOS + YPOS)
        self.window.geometry("650x500+100+200")
        
        self.onFrameConfigure(None)
    
    def createMainClassesWindow(self):
        self.drawMainClassesWindow()
        self.window.mainloop()
        
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        #self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=600,height=200)
    
    # Adds the class item to the main list and displays it in the scroller
    # form.
    def add_item(self):
        class_name = self.txt_name_val.get()
        class_descr = self.txt_descr_val.get()
        
        if class_name == "":
            return

        # if we're editing an item, then edit it, otherwise save a new one
        if self.item_id_being_edited > -1:
            for item in self.all_items:
                if item.si_id == self.item_id_being_edited:
                    item.name = class_name
                    item.descr = class_descr
            self.item_id_being_edited = -1
            self.add_button_name.set("Add " + self.context_of_item)
        else:
            # Creating a new SalesItem
            self.all_items.append(si.SalesItem(self.number_of_entries + 1, class_name, class_descr))
        
        # Displaying the new list on the screen.
        self.add_all_items_to_scroller()
        
        self.number_of_entries += 1
        
        self.txt_name_val.set("")
        self.txt_descr_val.set("")
        
    # Adds all items to the scroller to be seen and be able to pick for
    # editing or deleteing.
    def add_all_items_to_scroller(self):
        # First clearing the frame
        for widget in self.frmItems.winfo_children():
            widget.destroy()
        
        # table header first
        self.setUpTableHeader()

        # Now adding the items from the collection
        row_counter = 1
        for item in self.all_items:
            self.add_item_row_to_scroller(row_counter, item)
            row_counter += 1

    # Add a single row of the items to the scroller
    # This needs to be used while iterating through all items.
    def add_item_row_to_scroller(self, row_counter, item):
        lblID = tk.Label(self.frmItems, text=item.si_id, fg="blue", font=("Arial", 10))
        lblID.grid(row=row_counter, column=0)
        
        lblName = tk.Label(self.frmItems, text=item.name, fg="blue", font=("Arial", 10))
        lblName.grid(row=row_counter, column=1)
        
        lblDescr = tk.Label(self.frmItems, text=item.descr, fg="blue", font=("Arial", 10))
        lblDescr.grid(row=row_counter, column=2)

        # Edit button        
        edit_action = partial(self.load_item, item.si_id)
        btnEdit = tk.Button(self.frmItems, text="Edit", command=edit_action)
        btnEdit.grid(row=row_counter, column=3)

        # Delete button        
        delete_action = partial(self.delete_item, item.si_id)
        btnDelete = tk.Button(self.frmItems, text="Delete", command=delete_action)
        btnDelete.grid(row=row_counter, column=4)

    # loads item identified by its ID to allow editing it.
    def load_item(self, item_id):
        for item in self.all_items:
            if item.si_id == item_id:
                self.txt_name_val.set(item.name)
                self.txt_descr_val.set(item.descr)
                self.item_id_being_edited = item.si_id
                break

        self.add_button_name.set("Save " + self.context_of_item)

    # deletes class identified by its ID
    def delete_item(self, item_id):
        new_item_list = []
        for item in self.all_items:
            if item.si_id != item_id:
                new_item_list.append(item)
            
        self.all_items = new_item_list
        
        self.add_all_items_to_scroller()
    
    # Sets up table header for the sales items that will be added later
    def setUpTableHeader(self):
        lblID = tk.Label(self.frmItems, text="ID", fg="red", font=("Arial", 10))
        lblID.grid(row=0, column=0)
        
        lblName = tk.Label(self.frmItems, text="Name", fg="red", font=("Arial", 10))
        lblName.grid(row=0, column=1)
        
        lblDescr = tk.Label(self.frmItems, text="Description", fg="red", font=("Arial", 10))
        lblDescr.grid(row=0, column=2)
    
    # Opens the window that lets adding sales items with the entered classes
    # choosable parents.
    def open_sales_items_window(self):
        import AddSalesItems as asi
        # current window needs to close first, because in the 
        # "createSalesItemInputWindow" we'll call self.window.mainloop()
        # which will not return for some time.
        self.window.destroy()
        si_win = asi.AddSalesItems(self.all_items)
        si_win.createSalesItemInputWindow()