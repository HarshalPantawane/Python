# 1 if-elif-else(syntax)

"""
if(condition):
  statement1
elif(condition):
  statement2
else:
  statementN
      
"""

 



# age = 23

# if(age <= 18):
#     print("minor")
# elif(18 < age < 60):
#     print("young and family man")    
# else:
#     print("senior citizen")
# # ^
# # |
# # that space is indentation, used insted of {}       
    
# print(age)     


# if we using if-elif-else statement and get both or all condition true , in that case first true condition statement will print. 

# Grade student base on marks
# marks >= 90, grade = "A"
# 90 > marks > 80, grade = "B"
# 80 > marks > 70, grade = "c"
# 70 > marks, grade = "d"

# marks = int(input("Enter total marks: "))

# if(marks > 90):
#     print("grade = A")
# elif(90 > marks > 80):
#     print("grade = B")
# elif(80 > marks > 70):
#     print("grade = C")
# elif(70 > marks):
#     print("grade = D")    
    
# print("all the best")    

# or 

# marks = int(input("Enter marks: "))

# if(marks >= 90):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C" 
# else: 
#     grade = "D"       
# print( "grade of student: ", grade)    

#################################

# nesting menas if inside if statement 

# syntax

# if(condition):
#     if(condition):
#         statement1
#     else:
#         statementN    
# else:
#     statementN          

# e.g,
age = int(input("Enter your age: "))

if(age > 18):
    if(age > 80):
        print("cannot drive")
    else:
        print("can drive")    
else:
    print("cannot drive")        