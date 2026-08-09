# marks = [10,11,12,13,4]
# print(marks)
# print(type(marks))

# # to find any perticular index
# print(marks[2])
# print(len(marks))

# we can store difff data types. (str, int, float) in pyhton
# string are immutable in pythin but list are mutable(can change)

# student = ["Harshal", 22, "Aroli", 122, 1.68]

# print(student)
# print(len(student))
# print(type(student))

# change value in list.
# student[2] = "Nagpur"  
# print(student)

# we cant add  new index in list.



# slicing is possible in list 

# marks = [10,12,14,13,15]

# # print(marks[1:4])
# # print(marks[:4])
# # print(marks[0:])
# print(marks[-5:-1])


# list method
"""
list = [2,1,3]

1. list.append(3) # adds one elelment at the end [2,1,3,4]

2. list.sort()    # sort in according order   [1,2,3]

3. list.sort(reerse=True) # sort in descending order

4. list.reverse()  # reverse list 

5. list.insert(idx, el)   # insert element at index

6. list.remove()       # remove first occcurrence of element

7. list.pop(idx)       # removes element at idx

"""

# append
# list = [1, 2, 3, 4, 5, 6]

# list.append(7)  # 7 is value, not index
# print(list)



# sorting
# marks = [45,76,21,54,91,26]

# print(marks.sort())   # it will print Noe because it doesnt have to print something, just make change.    
# print(marks)          # print updated list

# output [21, 26, 45, 54, 76, 91]



# reverse sort
# marks = [45,76,21,54,91,26]

# print(marks.sort(reverse=True))
# print(marks)

# its possible in string also.
# list = ["a", "s", "d", "f", "g", "b"]

# list.sort(reverse=True)
# # print(list.sort(reverse=True))  # or list.sort(reverse=True)
# print(list)



# reverse 
# list = ["a", "s", "d", "f", "g", "b"]

# list.reverse()     # doing reverse like ['b', 'g', 'f', 'd', 's', 'a']
# print(list)




# list.index
# list = [45,76,21,54,91,26]
# list = ["a", "s", "d", "f", "g", "b"]


# # list.insert(idx,el)        add element at index
# # list.insert(3,55)
# list.insert(3,"h")
# print(list)



# list.remove
# list = [45,76,21,54,91,76,26]
# list = ["a", "s", "d", "f", "g", "b"]

# list.remove(76)       
# list.remove("s")       # it remove only first occurrence 
# print(list)


# list.pop
# list = [45,76,21,54,91,76,26]
# list = ["a", "s", "d", "f", "g", "b"]

# list.pop(2)
# print(list)