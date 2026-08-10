## loop is used to repeat instructuon.
"""
1. while loop
 
    syntax:
    while condition:
        #some work
    
    
2. for loop
   
   syntax: 
   
     
    
"""
## 1 while loop

## initialization
# count = 1            # iterator

# # condition
# while count <= 5:    # 1 run means 1 iteration
#     print("hello")
#     # state update
#     count += 1


# i = 1

# while i <= 10:
#     print(i)
#     i += 1



## for reverse

# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# print("loop ended")    

## 1. print num from 1 to 100

# i = 1
# while i <= 100:
#     print(i)
#     i += 1
# print("loop ended")    

## 2. print number from 100 to 1


# i = 100
# while i >= 1:
#     print(i)
#     i -= 1
# print("loop ended")    

## 3. print the multiplication table of a number n.

# n = int(input("Enter number: "))
# i = 1
# while i <= 10:
#     print(n * i)
#     i += 1
# print("table completed")    


## 4. print the elements of the following list using a loop.

# num = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(num):
#     print(num[idx])
#     idx += 1

## or 

# i = 1
# while i <= 10:
#     print(i * i)
#     i += 1
# print("completed")    


## 5. search for a number x in this tuple using loop
# num =  (1,4,29,16,25,36,64,81,100)

# x =  int(input("E nter you no: "))
# i = 0

# while i < len(num):
#     if(num[i] == x):
#         print("found at idx", i)
#         break
#     i += 1    



##  break and continue
# break: used to terminate the loop when encountered.

# continue: terminates execution inthe current iteration and continue execution of the loop with next iteration


# i = 1
# while i <= 5:
#     print(i)
#     if(i ==3):
#         break     # break loop
#     i += 1
    
    
# i = 0
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue      # it will skip 3, continue means skip
#     print(i)
#     i += 1    


## for odd num    
# i = 0
# while i <= 10:
#     if(i%2 == 0):
#         i += 1
#         continue
#     print(i)
#     i += 1    
    
## for even num     
# i = 0
# while i <= 10:
#     if(i%2 != 0):
#         i += 1
#         continue
#     print(i)
#     i += 1   
######################################################################

# for loop
# for sequential traversal. for traveling list , string, tuples etc.

# syntax 
    # for el in list:
        # some work
 
    
# for loop with else 
    # for el in list:
        # some work
    # else:   
        # work when loop ends
        

# num = [1,2,3,4,5]

# for val in num:
#     print(val)        

        
# tup = (1,2,3,4,5,6)

# for num in tup:
#     print(num)        
        
        
        
# str = "harshalpantawane"
# for char in str:
#     print(char)        
# else:
#     print("end")     # this is optinal no need if
    



# # 1. print th element of the following  list using a loop.
# num = [1,4,9,16,25,36,64,81,100]
# for val in num:
#     print(val)
# else: 
#     print("end")    
    

## 2. search for a number x in this tuple using loop     # this is linear search
# num = (1,4,9,16,25,36,64,81,100,25)
# x = 25

# idx = 0
# for val in num:
#     if(x == val):
#         print("found at idx", idx)
#         # break
#     idx += 1
# else:
#     print("not found")     


###########################################
## range()
# range is functions return a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stop before a specified number.

# syntax
# range(start?, stop, step?)

# for el in range(5):
#     print(el)
    
# for el in range(1,5):
#         print(el)
        
# for el in range(1, 5, 2):
#     print(el)        

# 1.
# # given inly stop condition
# seq = range(5)   
# # start with 0 and ending will not included
# for i in seq:
#     print(i) 

## 2 
# seq = range(10)

# for i in range(1, 10): # set start from
#     print(i)

## 3
# seq = range(10)

# for i in range(1, 10, 2):    # set step add by 2
#     print(i)
    
    
## 4 print even num 
# for i in range(2, 100, 2):
#     print(i)  


####################################################
# pass statement
# pass is a null statement that does nothing. it is used as a for future code.

# syntax
#   for el range(10):
#       pass

for el in range(5):
    pass              # if dont want to do enything
print("ok")    