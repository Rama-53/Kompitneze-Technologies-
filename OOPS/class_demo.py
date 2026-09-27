
# class Student:
#    pass
# student1=Student()
# student2=Student()
# student1.name="deepu"
# student1.age=20
# student1.course="python"

# student2.name="jithu"
# student2.age=20
# student2.course="python"

# print(student1.name)

"""class Student:

    def __init__(self, name, age):#init  is a special methode that automaticaaly runs when we create an object it is mainly used to intilize the objects data
        self.name=name
        self.age=age

    def display(self):
        print(self.name)
        print(self.age)

student1=Student("arun",21)
student2=                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Student("rahul",22)

print(student1.display())
print(student2.display())"""

"""
class Employee:
    company="abc company" #company is a class attribute 
    def __init__(self,empl_name):
        self.empl_name=empl_name
e1=Employee("deepu")
e2=Employee("jithu")

print(e1.empl_name,e2.empl_name) #e1,e2 -> instance attrtibutes
print(e1.company)"""


#scope 
"""class Student:
    school = "Abc-school" #accesbale in all instanace of class(class variable)
    def __init__(self,name):
        print(self.school)
        self.name = name #instance scope- accessible only via objects(instance varbale)
    
    def show(self):
        marks=90    #local scope-accessible only inside instance method(local variabl)
        print(self.school)
        print(self.name,marks)

s1=Student("Ram")
s1.show()
print(s1.name)

---------------------------------
OUTPUT
----------------------------------
Abc-school
Abc-school
Ram 90
Ram

"""

"""Shadowing varbale """


#shading(shadowing variable)
"""class Student:
school="abc school"
def __init__(self,name):
    self.name=name
    self.school="xyz"
    print (self.school)
def show(self):
    marks=90
    print (self.school)
    print(self.name,marks)
    print (marks)
student1=Student("Jithu")
student1. show()
print(Student.school)
print(student1.name)

class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    def bark(self):
         print("Dog barks")
s1=Dog()
s1.bark()
s1.speak()
"""
"""#Multilevel Inheritance
class GrandParent:
    def __init__(self):
        self.house="Big House"
    def show_grandparent(self):
        print(self.house)
class Parent(GrandParent):
    def __init__(self):
        super().__init__()
        self.car="BMW"
    def show_car(self):
        print(self.car)
class Child(Parent):
    def _init_(self):
        #super() ._ init_()
        self.bike="Royal Enfiled"
    def show_bike(self);
        print(self.bike)
s1=Child()
s1.show_grandparent ()
s1.show_car()
s1.show_bike()""" 


#MLTIPLE iNheritance

class Father:
    def init_(self,house):
        self.house=house
        print("Fathers house")
class Mother(Father):
    def _init_(self):
        super() .__init__()
        self.car="mothers car"
class Child(Mother):
    def _init_(self):
        super() .__init__()
        self.name="Aiswarya"
c=Child()