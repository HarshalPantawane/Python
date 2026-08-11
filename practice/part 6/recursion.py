# recursion 
# when a function calls itslef repeatedly.

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)
#     print("end")
# show(5)              # rapidly calling fun is call stack  

# recursion via factorial

# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n
# print(fact(4))

# practice
# 1. Write a recursion function to calculate the sum of first natural numbers.

# def calc_sum(n):
#    if(n ==0):
#      return 0
#    return calc_sum(n-1) + n

# sum = calc_sum(5)
# print(sum)   


# 2. write a recursive function to print all element  in a list. 
# Hint : use list and index as parameter

from os import name


def print_list(list, idx=0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

names = ["harshal","sriya","garu","anna"]

print_list(names)