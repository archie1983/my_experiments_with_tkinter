# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 21:18:04 2020

A container class for the main class object as well as the
sales item object.

@author: aelksnis
"""
import ntpath

class SalesItem:

    def __init__(self, 
                 si_id, 
                 name, 
                 descr, 
                 price = 0, 
                 page = 0, 
                 pic_full_path = "",
                 parent_id = 0):
        self.si_id = si_id
        self.name = name
        self.descr = descr
        self.price = price
        self.page = page
        self.pic_full_path = pic_full_path
        self.parent_id = parent_id

    @property
    def pic_short_path(self):
        return self.__pic_file
        
    @property
    def pic_full_path(self):
        return self.__pic_full_path

    @pic_full_path.setter
    def pic_full_path(self, pic_full_path):
        self.__pic_full_path = pic_full_path
        if pic_full_path != "":
            _, self.__pic_file = ntpath.split(pic_full_path)
        else:
            self.__pic_file = ""
            
    def csv_line(self):
        result = str(self.si_id) + "," + \
                self.name + "," + \
                self.descr + "," + \
                str(self.price) + "," + \
                str(self.page) + "," + \
                str(self.parent_id) + "," + \
                self.pic_short_path + "," + \
                self.pic_full_path
                
        return result