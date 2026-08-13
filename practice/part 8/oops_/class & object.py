# to map with real world scenarios, we started using objects in code.
# this is called object oriented programming


# class is a blueprint for creating objects.

"""
syntax

# creating class       it is used to store info about something in profesional way insted of list.

class Class_name:   #name always start with capitals later
  name = "harshal pantawane"
  
# creating object (instance) 
s1 = Class_name()
print(s1.name)  
"""

# ex

# class Car:         
#     color = "black" 
#     model = 2025
    
# c1 =  Car()
# print(c1)
# print(c1.color)    
##################################

# constructor
# all classes have a function called _init_(), which is always executed when the object is beig initiated.
"""
syntax
class Class_name:
  def __init__(self):    #self attribute used for its own constructor
      print("adding new student in database..")
      
c1 = Class_name()           # this parenthesis used to call constructor  
# constructor willl called automaticaly
    
"""
# class Car:   
#     name = "BMW"
#     # constructor always need one argument that is self(argument is mutable)
#     def __init__(self):         # this will print automaticly location (same)
#         print(self)
#         print("adding new car model")
        
# c1 = Car()
# print(c1)    # it is manualy printing location (same)
        
        
# class Car:
#     name = "BMW"        
#     def __init__(me, model):  #but always used self
#         me.model  = model 
#         print("adding new model")

# c1 = Car("2025")   
# print(c1.model)     # we are using print for print model parameter



# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database")
        
# s1 = Student(22, "harshal")
# print(s1.marks, s1.name)   

# s2 = Student("rana", 25)
# print(s2.name, s2.marks)




# # this is default constructor
# there are two type of constructure

# # if you create or not , python will create for you
# class Student:
#     # default constructor
#     def __init__(self):        
#         pass
    
#     # parameterized constructor    
#     def __init__(self, name, bases):
#         self.name = name
#         self.bases = bases
            
# s1 = Student("nana", "peddanana")
# print(s1.name, s1.bases)


"""
# calss and instance attributes   --- parameter
clss.attr
obt.attr
"""

# ex
# class Student:
#     # this is class attribute
#     # this is common for all that why we store directly
#     college_name = "babasaheb ambedkar college"
    
#     def __init__(self, name, marks):
#         # object attributes
#         self.name = name
#         self.marks = marks
#         print("adding student data")      # this wil print first before name and marks

# s1 = Student("goma", 21)
# print(s1.name, s1.marks)        
# print(s1.college_name)

# s2 = Student("sanga", 55)
# print(s2.name, s2.marks)
# # print(s2.college_name)       # / print(Student.college_name) this is also completely valid
# print(Student.college_name)





# in class and object attribute, always object attribute have preference 
# class Student:
#     name = "unknown"
#     def __init__(self,name, marks):
#         self.name  = name
#         self.marks = marks
#         print("adding data in database..")

# s1 = Student("sriya", 22)        
# print(s1.name, s1.marks)



"""
mehtods
method are function that belong to objects.

class Student:
  def __init__(self, name):
    self.name = name
    
  # define method  
  def hello(self):
    print("hello", self.name) 
    
s1 = Student("harshal")    
s1.hello()
"""

# class Car:
#     def __init__(self, name, model):
#         self.name = name
#         self.model = model
      
#     # define method    
#     def brend(self):
#         print("BMW", self.name)  
        
#     def get_model(self):
#         return self.model
                  
# c1 = Car("s11",2025) 
# c1.brend() 
# print(c1.get_model())


# practice
# create student class that takes name and marks of 3 subjects as argument in constructor. then create method to print the average.

# class Student:
#     def __init__(self, name, sub1, sub2, sub3):
#         self.name = name
#         self.sub1 = sub1
#         self.sub2 = sub2
#         self.sub3 = sub3
        
#     def get_avg(self):
#         avg = (self.sub1 + self.sub2 + self.sub3) / 3
#         print("average is : ",avg)    

# s1 = Student("harshal", 12,13,14)
# print(s1.name, s1.sub1,s1.sub2,s1.sub3)
# s1.get_avg()        

# or 

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg is : ", sum/3)       

# s1 = Student("harshal", [12,13,14])
# # if i want to change attribute name
# s1.name = "sriya"
# s1.get_avg()        



"""
static method
methods that don't use the self parameter(work at class level)

syntax

   class Student:
      @staticmethod  # decorator
      def college():
        print("ABC College")
        
# decorator allow us to wrap another function in order 
# to extend the behaviour of the wrapped function,
# without permanently modifying it.     
"""

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     @staticmethod    # decorator
#     def hello():
#         print("hello")    
        
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg is : ", sum/3)       

# s1 = Student("harshal", [12,13,14])
# # if i want to change attribute name
# s1.name = "sriya"
# s1.get_avg() 
# s1.hello()     

