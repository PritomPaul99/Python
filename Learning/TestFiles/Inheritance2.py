# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 07:30:21 2022

@author: ASUS
"""

class A:
  def __init__(self,name,age):
      self.name=name
      self.age=age
      print("I am A")
  
      
  def print_A(self):
      print(self.name,self.age,end=" ")





class B(A):
    #override
    def __init__(self,name,age,sex):
      A.__init__(self,name,age)
      self.sex=sex
      print("I am B")
      
    def print_B(self):
       super().print_A()
       print(self.sex)
    @classmethod
    def init_B(cls,string):
        s=string
        return cls(*s.split('-'))

child_object=B("Arafat",24,'M')
child_object.print_B()
child_object2=B.init_B("Pritom-24-M")
child_object2.print_B()

