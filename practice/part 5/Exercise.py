# using for and range
# 1. print num from 1 to 100.

# for i in range(1, 101):
#     print(i)
    
## 2.  from 100 to 1
# for el in range(100, 0, -1):
#     print(el)

## 3. multiplication of n
# i = int(input("Enter nu: "))
# for el in range(1, 11):
#     print(i * el)




## 4. WAP to find the sum of first natural number. (using while)
# i = 1
# n = 10

# sum = 0
# while i <= n:
#     sum += i
#     i += 1
# print(sum)


## using for loop

# n = 10
# sum = 0
# for el in range(1,n+1):
#     sum += el
# print(sum)    


## 5. WAP to find the factorial of first n num. (using for loop)


# fact = 1
# i = 1
# n = 5
# while i <= n:
#     fact *= i
#     i +=1
# print(fact)    


# for loop
fact = 1
n = 5
for i in range(1, n+1):
    fact *= i
print(fact)    