# a built-in data type that lets us create immutable sequence of values.
# used perinthesis() in tuples

# tup = (2,1,3,4,5)
# print(type(tup))
# print(tup[2])
# # tup[2] = 9  # its not possible


# empty tuple is valid in tuples
# tup = ()

# tup1 = (1,)  # it is tuple element, for single value use ","
# tup2 = (1)   # it will assume as integer value
# tup3 = ("harshal")

# print(type(tup))         # tuple
# print(type(tup1))        # tuple 
# print(type(tup2))        # int
# print(type(tup3))        # str
# # output is ()



# slicing is possible in tuple



# tuple method
"""
tuple = (2,1,3)

1. tup.index(el)   # return index of first occurrence

2. tup.count(el)   # count total occurrence
"""

# index
# tup = (2,1,3,2,7,4,5,7)

# print(tup.index(2))   # print idx of value,  2 is value


# count
tup = (2,1,3,2,7,4,5,7)

print(tup.count(3))   