# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 10:03:00 2022

@author: ASUS
"""

from numpy import random

x=random.randint(100)
print(x)


x=random.rand()
print(x)
#Generating Random Array

array=random.randint(100,size=(5))
print(array)

#Generating a 2D array

TwoD=random.randint(100,size=(2,5))
print(TwoD)


x = random.rand(3, 5)

print(x)

#take a array and returns a random number 
arr=random.choice([1,2,3,4,5])
print(arr)

#Generate a 2d array that contains random Number
arr=random.choice([1,2,3,4,5],size=(2,5))
print(arr)