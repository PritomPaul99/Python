# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 00:52:54 2022

@author: ASUS
"""

dict={}
print("Enter the number of Keys:")
n=int(input())
for x in range(0,n):
    key,value=input().split()
    dict[int(key)]=value

print(dict)    
