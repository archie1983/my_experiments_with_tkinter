# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:32:37 2020

@author: aelksnis
"""
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd

# Allow entry of sales items.
class AddSalesItems:

    def __init__(self, top_classes):
        self.window = tk.Tk()
        
        # variables holding the input values
        self.txt_name_val = tk.StringVar(self.window)
        self.txt_descr_val = tk.StringVar(self.window)
        self.parentSelection = tk.StringVar(self.window)
        self.int_price = tk.IntVar(self.window)
        self.int_page = tk.IntVar(self.window)
    
        # number of entries added
        self.number_of_entries = len(top_classes)
        self.top_classes = [""] + top_classes
        
        self.current_item_row = 0
    
    # Creates the window of sales item entry
    def createSalesItemInputWindow(self):
        row_num = 0
        # Name of the item
        lblName = tk.Label(self.window, text="Item name", fg="black", font=("Arial", 10), width="10")
        lblName.grid(row=row_num, column=0)
        txtName = tk.Entry(self.window, width=30, textvariable=self.txt_name_val)
        #txtName.insert(tk.END, "Class name")
        txtName.grid(row=row_num, column=1)
        row_num += 1
    
        # Description of the item
        lblDescr = tk.Label(self.window, text="Item description", fg="black", font=("Arial", 10))
        lblDescr.grid(row=row_num, column=0)
        txtDescr = tk.Entry(self.window, width=30, textvariable=self.txt_descr_val)
        txtDescr.grid(row=row_num, column=1)
        row_num += 1

        # Parent class drop down box
        lblTopClass = tk.Label(self.window, text="Top class", fg="black", font=("Arial", 10))
        lblTopClass.grid(row=row_num, column=0)
        self.parentSelection.set(self.top_classes[0]) # default value
        optParent = tk.OptionMenu(self.window, self.parentSelection, *self.top_classes)
        optParent.grid(row=row_num, column=1)
        row_num += 1

        # Price of the item
        lblPrice = tk.Label(self.window, text="Item price", fg="black", font=("Arial", 10))
        lblPrice.grid(row=row_num, column=0)
        txtPrice = tk.Entry(self.window, width=5, textvariable=self.int_price)
        txtPrice.grid(row=row_num, column=1)
        row_num += 1

        # Page of the item
        lblPage = tk.Label(self.window, text="Item page", fg="black", font=("Arial", 10))
        lblPage.grid(row=row_num, column=0)
        txtPage = tk.Entry(self.window, width=5, textvariable=self.int_page)
        txtPage.grid(row=row_num, column=1)
        row_num += 1

        # Button for selecting an image for the new sales item
        btnChooseImg = tk.Button(self.window,
                           text="Choose image",
                           command=self.selectJPEG)
        btnChooseImg.grid(row=row_num, column=0)
        
        self.lblImage = tk.Label(self.window)
        self.lblImage.grid(row=row_num, column=1)
        row_num += 1

        # Frame containing current items
        # 1st creating a form where we'll keep a scrolling canvas
        frmScroller4Classes = tk.Frame(self.window,
            border=1,
            relief=tk.GROOVE,
            background="blue")
        frmScroller4Classes.grid(row=row_num, column=0, columnspan=2, sticky=tk.N+tk.S)
        
        # Creating canvas on scroller frame
        self.canvas = tk.Canvas(frmScroller4Classes)
        self.canvas.grid(row=0, column=0)
        
        # Creating scrollbar for the canvas, which will be on the same scroller frame.
        myscrollbar = tk.Scrollbar(frmScroller4Classes,orient="vertical",command=self.canvas.yview)
        myscrollbar.grid(row=0, column=1, sticky=tk.N+tk.S)
        
        # New frame for the contents on the canvas.
        
        # Frame containing current items
        self.frmClasses = tk.Frame(self.canvas)
        self.canvas.configure(yscrollcommand=myscrollbar.set)
        self.canvas.create_window((0,0),window=self.frmClasses,anchor='nw')
        self.frmClasses.bind("<Configure>", self.onFrameConfigure)
        row_num += 1
    
        # The header for the table holding current items
        self.setUpTableHeader()
    
        # Buttons for quitting and adding the new class
        btnAddItem = tk.Button(self.window,
                           text="Add Item",
                           command=self.add_item)
        btnAddItem.grid(row=row_num, column=0)
        
        button = tk.Button(self.window, 
                           text="QUIT", 
                           fg="red",
                           command=self.window.destroy)
        button.grid(row=row_num, column=1)
        
        # add title
        self.window.title("Check Out Data Entry - Sales Items")
        
        # set frame and geometry (width x height + XPOS + YPOS)
        self.window.geometry("500x500+100+200")
        
        self.onFrameConfigure(None)
        
        self.window.mainloop()
        
    # Required for scrolling frame
    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        #self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=400,height=200)
    
    # Adds sales item
    def add_item(self):
        class_name = self.txt_name_val.get()
        class_descr = self.txt_descr_val.get()
        top_class_name = self.parentSelection.get()
        top_class_id = 0
        item_price = self.int_price.get()
        item_page = self.int_page.get()
        cur_row = 0
        
        if class_name == "":
            return
        
        lblID = tk.Label(self.frmClasses, text=(self.number_of_entries + 1), fg="blue", font=("Arial", 10))
        lblID.grid(row=self.current_item_row, column=0)
        
        lblName = tk.Label(self.frmClasses, text=class_name, fg="blue", font=("Arial", 10))
        lblName.grid(row=self.current_item_row, column=1)
        
        lblDescr = tk.Label(self.frmClasses, text=class_descr, fg="blue", font=("Arial", 10))
        lblDescr.grid(row=self.current_item_row, column=2)
        
        lblParent = tk.Label(self.frmClasses, text=top_class_name, fg="blue", font=("Arial", 10))
        lblParent.grid(row=self.current_item_row, column=3)

        lblPrice = tk.Label(self.frmClasses, text=item_price, fg="blue", font=("Arial", 10))
        lblPrice.grid(row=self.current_item_row, column=4)
        
        lblPage = tk.Label(self.frmClasses, text=item_page, fg="blue", font=("Arial", 10))
        lblPage.grid(row=self.current_item_row, column=5)
        
        self.current_item_row += 1
        self.number_of_entries += 1
        
        self.txt_name_val.set("")
        self.txt_descr_val.set("")
        self.parentSelection.set("")
        self.int_price.set(0)
        
    # Sets up table header for the sales items that will be added later
    def setUpTableHeader(self):
        lblID = tk.Label(self.frmClasses, text="ID", fg="red", font=("Arial", 10))
        lblID.grid(row=self.current_item_row, column=0)
        
        lblName = tk.Label(self.frmClasses, text="Name", fg="red", font=("Arial", 10))
        lblName.grid(row=self.current_item_row, column=1)
        
        lblDescr = tk.Label(self.frmClasses, text="Description", fg="red", font=("Arial", 10))
        lblDescr.grid(row=self.current_item_row, column=2)
        
        lblParent = tk.Label(self.frmClasses, text="Parent", fg="red", font=("Arial", 10))
        lblParent.grid(row=self.current_item_row, column=3)

        lblPrice = tk.Label(self.frmClasses, text="Price", fg="red", font=("Arial", 10))
        lblPrice.grid(row=self.current_item_row, column=4)
        
        lblPage = tk.Label(self.frmClasses, text="Page", fg="red", font=("Arial", 10))
        lblPage.grid(row=self.current_item_row, column=5)
        
        self.current_item_row += 1

    def selectJPEG(self):
        path = fd.askopenfilename(filetypes=[("Image File",'.jpg')])
        print("P: ", path)
        
        im = Image.open(path)
        im = im.resize((75, 75), Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(im)
        #myvar=Label(root,image = tkimage)
        self.lblImage.image = tkimage
        self.lblImage.configure(image=tkimage)
        return path