# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 01:15:04 2022

@author: ASUS
"""

class Student:
    
    university_name="North East University of Bangladesh,Sylhet"
    
    def __init__(self,name,id):
        print("I am called during creation of object because i am a construcctor")
        self.name=name
        self.id=id
    def print_object(self):
       print("Name:",self.name,"Roll:",self.id,self.university_name)
       
    @classmethod
    def assign_with_string(cls,string):
        
        return cls(*string.split("-"))
    @staticmethod
    def print_normally():
        print("I am normal")
        
        
s1=Student("Arafat",13) 
s1.print_object() 
s2=Student.assign_with_string("Pritom-63")
s2.print_object()
s1.print_object()
s1.print_normally()
      
    