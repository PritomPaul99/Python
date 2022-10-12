# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 08:53:38 2022

@author: ASUS
"""

name="Arafat"
age=20
x=name
y=age
string="{name} is a bad boy from age {age}"
print(string.format(name=x,age=y))
string2="{0} is a bad boy from age {1}"
print(string2.format("pritom",20))