# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 03:01:50 2022

@author: ARAFAT
"""
class person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("I am super")
        
    def print_person_detail(self):
        print("Name:",self.name)
        print("Age:",self.age)

class student(person):
     #Inherit-class-Person(single Inheritance)
     varsity="NEUB"
     
     def __init__(self,name,age,id,sex):
          self.name=name
          self.age=age
          self.id=id
          self.sex=sex
          print("I am sub")
          
          
     def print_student(self):
         print(self.id)
        

student1=student("Arafat", 24,"200103020013",'M')
student1.print_person_detail()        