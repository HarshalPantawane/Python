"""
del keyword
used to delete object properties or objects itself

syntax

del s1.name
del s1
"""
# # del 
# class Student:
#     def __init__(self, name):
#         self.name = name
        
# s1 = Student("harshal")        
# print(s1.name)
# del s1
# print(s1)    

"""
private(like) attribute and methods
Conceptual implementations like python

private attribute and methods are meant to ne used only 
within the class and are not accessible from outside the class.

syntax
self.__acc_pass   # simply use "__"before it 
"""
# # private
# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass         # we cant access outoff class
        
#     def acco_pass(self):
#         print(self.__acc_pass)    
        
# acc1  = Account("12345", "abcd")
# print(acc1.acc_no)  
# acc1.acco_pass()  



# class Person:
#     __name = "unknown"        # private class attribute
    
#     def __hello(self):            # private methode attribute
#         print("hello person!")
        
#     def welcome(self):
#         self.__hello()        
        
# p1 = Person()
# print(p1.welcome())        

########################################################################################3
"""
inheritance
when one class(child) derives the properties and methods of anothers class(parentbase).

syntax
class Parent:
 ........

class Child(parent):
..........
"""

# # ex
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")
        
#     @staticmethod
#     def stop():
#         print("car stop.")    
        
# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")        
# car2 = ToyotaCar("safari")        

# print(car1.name)
# print(car1.color)
# print(car2.name)
# car1.start()

"""
inheritance type
1. single inheritance     
   class Parent:
   
   
   class Child(Parent):

2. Multi-level inheritance
    class Base:
    
    
    calss Derived(Base):
    
    
    calss Derived1(Derived):

3. multiple inheritance

   class Parent1:
   
   class Parent2:
   
   class inherite:
      def __init__(self):
         print("inherited from parent1 and parent2")
         
"""
# multi level inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started..")
        
#     @staticmethod
#     def stop():
#         print("car stoped.")
        
# class Toyota(Car):
#     def __init__(self,brand):
#         self.brand = brand 
        
# class Fortuner(Toyota):
#     def __init(self,type):
#         self.type = type
        
# car1 = Fortuner("diesel")                
# car1.start()



# multiple inheritnce
# class A:
#     varA = "welcome to class A"
    
# class B:
#     varB = "welcome to class B"    
    
# class C(A,B):
#     varC = "welcome to class C"    
    
# c1 = C()

# print(c1.varA)
# print(c1.varB)
# print(c1.varC)    


# or 

# class A:
#     varA = "welcome to class A"
    
# class B:
#     varB = "welcome to class B"    
    
# class C(A,B):
#     varC = "welcome to class C"  
    
#     def __str__(self):
#         return f"{self.varA}\n{self.varB}\n{self.varC}"
          
    
# c1 = C()
# print(c1)    

"""
Super method
super() method is used to access method of the parent class.
"""

# class Car:
#     def __init__(self, type):
#         self.type = type
        
#     @staticmethod
#     def start():
#         print("car started..")
        
#     @staticmethod
#     def stop():
#         print("car stoped.")
        
# class Toyota(Car):
#     def __init__(self,brand):
#         self.brand = brand 
        
# class Fortuner(Car):
#     def __init__(self,name,type):
       
#         self.name = name
#         self.type = type
#         super().__init__(type)
#         super().start()
        
      
        
# car1 = Fortuner("legender","diesel")  
# print(car1.name,car1.type)           

"""
class method (this is decorator)
A class method  is bounded to the class and receive the class as an implicit first argument.
note-static method cant access or modify class state and generlly for utility.

syntax
class Student:
  @classmethod # decorator
  def college(cls):
    pass
    
# there are few method (decorator)
1. @staticmethod
2. @classmethod(cls)
3. instancemethod(self)    
"""
# class Person:
#     name = "unknown"
    
#     def changeName(self, name):
#         self.name = name
        
# p1 = Person()
# p1.changeName("rahul")        
# print(p1.name)
# print(Person.name)

# output is 
# rahul
# unknown

# but we want rahul on both place
# there are few ways to write this

# class Person:
#     name = "unknown"
    
#     def changeName(self, name):
#         self.__class__.name = "rahul"   # 1 way
#         Person.name = name              # 2 way
        
# p1 = Person()
# p1.changeName("rahul")        
# print(p1.name)
# print(Person.name)

# using class method

# class Person:
#     name = "unknown"
    
#     @classmethod           # decorator
#     def changeName(cls, name):
#         cls.name = name
        
# p1 = Person()
# p1.changeName("rahul")
# print(p1.name)
# print(Person.name)        
    
    
# property decorator
# we use @property decorator on any method in the class to use the method as a property.


# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"

# stu1 = Student(97,98,99)            
# print(stu1.percentage)

# teacher realize phy marks is wrong
# it's actualy 88


# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
        
 
#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"
        
# stu1 = Student(97,98,99)            
# print(stu1.percentage)

# stu1.phy = 88

# print(stu1.percentage)

#######################################################################################
"""
# polymorphism: Operator Overloading
# when the same operator is allowed to have different meaning according to yhe context.

poly --> many
morphs --. form


Operators and Dunder functions
a + b # addition           a.__add__(b)
a - b # subtraction        a.__sub__(b)
a * b # multiplication     a.__mul__(b)
a / b # division           a.__div__(b)
a % b # module             a.__mod__(b)

"""
# practice 
# @getter
# @setter

# print(1 + 2)   #3
# print("harshal" + "sriya")  # harshalsriya
# print([1,2,3,4] + [5,6,7,8])     # merge

# class Complex:
#     def __init__(self,real, img):
#         self.real = real
#         self.img = img
        
#     def showNumber(self):
#         print(self.real,"i +",self.img,"j") 
    
#     # adding    
#     def __add__(self,num1):
#         newReal = self.real + num1.real 
#         newImg = self.img + num1.img 
#         return Complex(newReal, newImg)
    
#     # for subtraction 
#     def __sub__(self,num1):
#         newReal = self.real - num1.real 
#         newImg = self.img - num1.img 
#         return Complex(newReal, newImg) 
        
# num = Complex(1,3)
# num.showNumber() 

# num1 = Complex(2,4)
# num1.showNumber()

# num2 = num + num1      # simple + doesnt work with complex, for that used dunder function
# num2.showNumber()    

# num3 = num - num1
# num3.showNumber()



# 1. define a circle class to create a circle with radius r using the cunstructor.
# define an Area() method of a class which calculate the area of a the circle.
# define a perimeter() method of the class which allows you to calculate the perimeter of the circle.


# class Circle:
#     def __init__(self, r):
#         self.r = r
        
#     def area(self):
#         return (22/7) * self.r ** 2
    
#     def perimeter(self):
#         return 2 * (22/7) *self.r
    
    
# c = Circle(14)     
# print(c.area())       
# print(c.perimeter())



# 2. define a employee class with attribute role, department and salary.this class also a showdetails() method.
# create an engineer class that inherits properties from employee and has additional attribute: name and age

# class Employee:
#     def __init__(self,role,dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary
        
#     def showDetails(self):
#         print("role = ",self.role)
#         print("dept = ",self.dept)
#         print("salary = ",self.salary)
            
# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("engineer", "IT","75000")
           
            
# e1 = Engineer("john", 40)            
# e1.showDetails()


# 3.

class Order:
    def __init__(self,  item, price):
        self.item = item
        self.price = price
        
    def __gt__(self, odr2):
        return self.price > odr2.price    

odr1 = Order("chips", 20)    
odr2 = Order("tea", 15)

print(odr1 < odr2)