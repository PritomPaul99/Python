# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:18:56 2022

@author: ARAFAT
"""

file=open("Arafat_info.txt","rt")
#Open Function returns a File object

#Read a single line from file
print(file.readline())

#Read Everything From a File:
#Reading From Address Because File pointer is pointing that line    
print(file.read()) 

#File close()
file.close()
   
#Again Opening
file=open("Arafat_info.txt","rt")
print(file.read(6+5))
#Reading File each line with iterator
for x in file:
    print(x)
    
file.close()    
