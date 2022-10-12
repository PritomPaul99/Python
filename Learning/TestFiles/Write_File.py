# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:35:51 2022

@author: ASUS
"""

#Creat a File
file_name=input()
file=open(file_name+".txt","a")
for x in range(0,3):
    s=input()
    file.writelines(s+'\n')
 
file=open("writing.txt",'r')
print(file.read())    
file.close()       
