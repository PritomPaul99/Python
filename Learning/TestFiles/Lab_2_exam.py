# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 11:55:34 2022

@author: Arafat
"""
class Grade:
    def __init__(self):
        self.name=""
        self.ATT=1
        self.TT=0
        self.MS=0
        self.SF=0



class Student(Grade):
    
    def __init__(self,id):
        Grade.__init__(self)
        self.id=id
        self.dict={"Algo":0,"Net":0,"AI":0,"Ml":0}
        
    def print_(self):
        print(self.ATT,self.TT)
        
    def select_sub(self,name):
        self.name=name
        self.dict[name]
    def Att(self,policy):
        print("Enter the number of class")
        class_=int(input())
        print("Enter the number of Present")
        present_=int(input())
        if policy==2:
            self.ATT=class_ - present_
        elif policy==1:
            present=(present_/class_)*100
            if present>=95 and present<=100:
                 self.ATT=10
            elif present>=90 and present<=94:
                 self.ATT=9    
            elif present>=81 and present<=85:
                 self.ATT=8    
            elif present>=75 and present<=80:
                 self.ATT=7 
            elif present>=71 and present<=74:
                 self.ATT=6
            elif present>=66 and present<=70:
                 self.ATT=5
            elif present>=61 and present<=65:
                 self.ATT=4
            elif present>=60 and present<=64:
                 self.ATT=3
            else :
                 self.ATT=1
                 
    def TT_(self,policy):
        print("Enter the tutorial number:")
        num=int(input())
        t=[]
        sum=0
        for x in range(0,num):
            x=float(input())
            t.append(x)
            sum+=x
        t.sort()
        if policy==1:
            self.TT=float(sum/num)
        elif policy==2:
            self.TT=float(t[num-1]+t[num-2])
            
    def MS_(self,ms):
     self.MS=float(ms)
    def SF_(self,sf):
     self.SF=float(sf) 
     
    def resuslt(self):
       print("Result of ",self.name,"=",self.TT+self.ATT+self.MS+self.SF)
       self.dict[self.name]=self.name,self.TT+self.ATT+self.MS+self.SF
s=Student(1) 
s.select_sub("Algo")
s.Att(2)
s.TT_(2)
s.MS_(24)
s.SF_(32)
s.resuslt()
print(s.dict["Algo"])

    

