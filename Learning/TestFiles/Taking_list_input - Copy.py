# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 00:34:22 2022

@author: ASUS
"""

list=[]
print("Enter the size of array:",end="")
max=0
n=int(input())
for x in range(0,n):
    y=int(input())
    list.append(y)
    if x==0:
     max=y
    elif max < y:
     max=y
    
print("My list:",list)

print("Maximum of the list:",max)
    