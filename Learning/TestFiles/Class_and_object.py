# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 03:04:51 2022

@author: ASUS
"""

class mathclass:
    #The static variable belongs to class
    c=10
    def __init__(self,a,b):
        #variable inside __init__() belongs to object
        self.a=a
        self.b=b
       
        
    def max_returner(math):
        if math.a>math.b:
            print(math.a)
        else :
            print(math.b)
          
    def min_returner(math):
        if math.a<math.b:
            print(math.a)
        else :
            print(math.b) 
            
    def add(self):
       print(self.a+self.b)         

      
p1=mathclass(2,3) 
p1.max_returner()
p1.min_returner()
print(mathclass.c)
p2=mathclass(5, 10)
p2.add()

      