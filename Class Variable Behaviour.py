# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:42:47 2017

@author: deepak
"""

#Behaviour of Class Variable

class Animals(object):
    def __init__(self,age,parent1,parent2):
        self.age=age
        self.name=None
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self,new_age):
        self.age=new_age
    def set_name(self,new_name=""):
        self.name=new_name
    def __str__(self):
        return "animal" + str(self.name) +":" +str(self.age)

class Rabbit(Animals):
    tag=1
    def __init__(self,age,parent1,parent2):
        Animals.__init__(self,age)
        self.parent1=parent1
        self.parent2=parent2
        self.r=Rabbit.tag
        Rabbit.tag +=1
        def get_r(self):
            return str(self.r).zfill(3)
        def get_parent1(self):
            return self.parent1
        def get_parent2(self):
            return self.parent2
        
        
peter=Rabbit(2)
peter.set_name("Paylu")
hopsy= Rabbit(3)
hopsy.set_name("Hari")

cotton=Rabbit(1,hopsy,peter)
cotton.set_name('Tuffy')
print(cotton)
print(cotton.get_parent2())

mopsy=peter+hopsy
mopsy.set_name('Murphy')
print(mopsy.get_parent1())
print(mopsy.get_parent2())
print(mopsy.get_name())


#methods to compare two Rabbits
def __eq__(self, other):
    parents_same = self.parent1.r == other.parent1.r \
                  and self.parent2.r == other.parent2.r
    parents_different = self.parent2.r == other.parent1.r \
                  and self.parent1.r == other.parent2.r
    return parents_same or parents_different











            
        
        
        
    