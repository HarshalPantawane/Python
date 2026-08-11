# function 
# block of statement that perform a specific task.
# used for redundant means repeat

"""
syntax
# function define
def func_name(parameter1, parameter2,....):
  # some work
  return val
  
# function call
func_name(agr1, arg2,...)  
"""

# 1.
# function definition 
# def calc_sum(a, b):
#     sum = a + b
#     print(sum)
#     return sum

# # function call
# calc_sum(12, 15)
    
# 2.    
# def calc_sum(a, b):
#     return a + b

# sum = calc_sum(1, 2)
# print(sum) 

# 3.
# def print_hello():  # we cal leave function empty
#     print("hello")
      
# print_hello()       

# 4.
# def print_hello():  # we cal leave function empty
#     print("hello")
      
# output = print_hello()       
# print(output)       # empty func give None

# # 5. average of 3 num
# def calc_avg(a,b,c):
#     sum = a + b + c
#     avg = sum / 3
#     print(avg)
#     return avg 
    
# calc_avg(10,15,20)    



##############################################
"""
functions type
# 1. built in function   # already written by someone else

> print()
> lena()
> type()
> range()

# 2. user define function   # written by us

"""
# 1.
# print("harshal", end =" ")
# print("sriya")
# output will harshal sriya

# print("harshal", end ="$")
# print("sriya")
# # output is harshal$sriya

# # 2. user define
# def calc_sum(b, a = 1): # b is non-default, a is default, non-default should be first.
#   print(a * b)
#   return a * b

# calc_sum(2)

# practice
# 1. WAP to print the length of a list.(list is to parameret)
# table = [11,12,13,14,15,16]

# def len_list(table):
#   print(len(table))
  
# len_list(table)  


# 2. WAP to print the element of a list in a single line.( list is the parameter)
# table = [11,12,13,14,15,16]


# def print_ele(table):
#   for el in table:
#     print(el, end = " ")
  
# print_ele(table) 


# heros = ["iron man","thor","hulk","loki","captain"]


# def print_ele(heros):
#   for el in heros:
#     print(el, end=" ")
  
# print_ele(heros) 


## 3.WAP to find the factorial of n.(n is the parameter)

# def calc_fact(n):
#   fact = 1
#   for i in range(1,n+1):
#     fact *= i
#     i += 1
#   print(fact)
    
# calc_fact(5)  

## 4. WAP to convert USD to INR.
# def con_cur(n):
#   inr = 90 * n
#   print("inr value is: ",inr,"inr")
  
# con_cur(2)  

# 5. find n num is even or odd

def idn_num(n):
  if(n%2 == 0):
    print("num is evev: ",n)
  else:
    print("num is odd: ",n)
    
idn_num(3)      