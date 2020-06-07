# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:32:37 2020

@author: aelksnis
"""
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
from functools import partial
import SalesItem as si
from AddClass import AddClass

# Allow entry of sales items.
class AddSalesItems(AddClass):

    def __init__(self, top_classes):
        super().__init__()
        
        self.top_classes = top_classes
        
        # additional variables holding the input values
        self.parentSelection = tk.StringVar(self.window)
        self.int_price = tk.IntVar(self.window)
        self.int_page = tk.IntVar(self.window)
    
        # number of entries added
        self.number_of_entries = len(top_classes)
        self.top_classes_names = [""]
        for tc in top_classes:
            self.top_classes_names.append(tc.name)
        
        # currently selected picture path
        self.current_pic_path = ""

        # number of entries added
        self.number_of_entries = 0
        
        # What we're editing - for string constants
        self.context_of_item = "Sales Item"

    # Creates the window of sales item entry
    def createSalesItemInputWindow(self):
        self.drawMainClassesWindow()
        # Parent class drop down box
        lblTopClass = tk.Label(self.frmInputs, text="Top class", fg="black", font=("Arial", 10))
        lblTopClass.grid(row=self.row_num, column=0)
        self.parentSelection.set(self.top_classes_names[0]) # default value
        optParent = tk.OptionMenu(self.frmInputs, self.parentSelection, *self.top_classes_names)
        optParent.grid(row=self.row_num, column=1)
        self.row_num += 1

        # Price of the item
        lblPrice = tk.Label(self.frmInputs, text="Item price", fg="black", font=("Arial", 10))
        lblPrice.grid(row=self.row_num, column=0)
        txtPrice = tk.Entry(self.frmInputs, width=5, textvariable=self.int_price)
        txtPrice.grid(row=self.row_num, column=1)
        self.row_num += 1

        # Page of the item
        lblPage = tk.Label(self.frmInputs, text="Item page", fg="black", font=("Arial", 10))
        lblPage.grid(row=self.row_num, column=0)
        txtPage = tk.Entry(self.frmInputs, width=5, textvariable=self.int_page)
        txtPage.grid(row=self.row_num, column=1)
        self.row_num += 1

        # Button for selecting an image for the new sales item
        btnChooseImg = tk.Button(self.frmInputs,
                           text="Choose image",
                           command=self.selectJPEG)
        btnChooseImg.grid(row=self.row_num, column=0)
        
        self.lblImage = tk.Label(self.frmInputs)
        self.lblImage.grid(row=self.row_num, column=1)
        self.row_num += 1

        # Remove the "Add Sales Items button" as we won't be opening this window
        # again from itself.
        self.btnAddItems.destroy()

        # add title
        self.window.title("Check Out Data Entry - Sales Items")
        
        # set frame and geometry (width x height + XPOS + YPOS)
        self.window.geometry("500x500+100+200")
        
        self.onFrameConfigure(None)
        
        self.window.mainloop()
    
    # Adds sales item
    def add_item(self):
        class_name = self.txt_name_val.get()
        class_descr = self.txt_descr_val.get()
        top_class_name = self.parentSelection.get()
        
        # finding the top class because we need its ID
        top_class_item = self.findTopClassFromItsName(top_class_name)
        if top_class_item is not None:
            top_class_id = top_class_item.si_id
        else:
            top_class_id = 0
        
        item_price = self.int_price.get()
        item_page = self.int_page.get()
        
        if class_name == "":
            return
        
        # Creating a sales item from the entered data and adding it to the list
        self.all_items.append(si.SalesItem(self.number_of_entries + 1,
                                              class_name,
                                              class_descr,
                                              item_price,
                                              item_page,
                                              self.current_pic_path,
                                              top_class_id))

        # Displaying the new list on the screen.
        self.add_all_items_to_scroller()
        
        self.txt_name_val.set("")
        self.txt_descr_val.set("")
        self.parentSelection.set("")
        self.int_price.set(0)
        self.int_page.set(0)
        self.current_pic_path = ""
        self.lblImage.image = None
        self.lblImage.configure(image=None)
        
        self.number_of_entries += 1        
        
    # Add a single row of the items to the scroller
    # This needs to be used while iterating through all items.
    def add_item_row_to_scroller(self, row_counter, item):
        top_class = self.findTopClassFromItsID(item.parent_id)
        
        if (top_class != None):
            top_class_name = top_class.name
        else:
            top_class_name = ""
        
        lblID = tk.Label(self.frmItems, text=item.si_id, fg="blue", font=("Arial", 10))
        lblID.grid(row=row_counter, column=0)
        
        lblName = tk.Label(self.frmItems, text=item.name, fg="blue", font=("Arial", 10))
        lblName.grid(row=row_counter, column=1)
        
        lblDescr = tk.Label(self.frmItems, text=item.descr, fg="blue", font=("Arial", 10))
        lblDescr.grid(row=row_counter, column=2)
        
        lblParent = tk.Label(self.frmItems, text=top_class_name, fg="blue", font=("Arial", 10))
        lblParent.grid(row=row_counter, column=3)

        lblPrice = tk.Label(self.frmItems, text=item.price, fg="blue", font=("Arial", 10))
        lblPrice.grid(row=row_counter, column=4)
        
        lblPage = tk.Label(self.frmItems, text=item.page, fg="blue", font=("Arial", 10))
        lblPage.grid(row=row_counter, column=5)

        # Delete button        
        delete_action = partial(self.delete_item, item.si_id)
        btnDelete = tk.Button(self.frmItems, text="Delete", command=delete_action)
        btnDelete.grid(row=row_counter, column=6)    
    
    # Sets up table header for the sales items that will be added later
    def setUpTableHeader(self):
        super().setUpTableHeader()
        lblParent = tk.Label(self.frmItems, text="Parent", fg="red", font=("Arial", 10))
        lblParent.grid(row=0, column=3)

        lblPrice = tk.Label(self.frmItems, text="Price", fg="red", font=("Arial", 10))
        lblPrice.grid(row=0, column=4)
        
        lblPage = tk.Label(self.frmItems, text="Page", fg="red", font=("Arial", 10))
        lblPage.grid(row=0, column=5)

    def selectJPEG(self):
        self.current_pic_path = fd.askopenfilename(filetypes=[("Image File",'.jpg')])
        #print("P: ", self.current_pic_path)
        
        im = Image.open(self.current_pic_path)
        im = im.resize((125, 125), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(im)
        #myvar=Label(root,image = tkimage)
        self.lblImage.image = tkimage
        self.lblImage.configure(image=tkimage)
        
        for sales_item in self.all_items:
            print(sales_item.csv_line())
        
        #return self.current_pic_path
    
    # Finds a SalesItem object in the main collection with a name matching
    # the given name.
    def findTopClassFromItsName(self, top_class_name):
        result = None
        for tc in self.top_classes:
            if tc.name == top_class_name:
                result = tc
            
        return result
    
    # Finds a SalesItem object in the main collection with an ID matching
    # the given ID.
    def findTopClassFromItsID(self, top_class_id):
        result = None
        for tc in self.top_classes:
            if tc.si_id == top_class_id:
                result = tc
            
        return result