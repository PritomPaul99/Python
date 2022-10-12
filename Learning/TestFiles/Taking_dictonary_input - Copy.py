# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 00:44:52 2022

@author: ASUS
"""

dict={}
print("Enter the number of key you wants:")
n=int(input())

for x in range(0,n):
    key=int(input())
    value=input()
    dict[key]=value
   
print(dict)    