# Dictionary are used to store data values in key:value pairs
# they are unorderd, mutable and don't allow duplicate key


# dict = {
#     # in values all data types valied and list and tuples too
#     "name" : "Harshal", 
#     "age"  : 23,
#     "genser" : "male",
#     "marks" : [23,21,52,22,20]
    
# }
# print(dict["name"])
# print(dict["age"])

# change value and add new value
# dict["name"] = "sriya"  # override, you can pass any data type
# dict["surname"] = "Pantawane"
# print(dict)

# you can start with null dict {}
# null_dict = {}



# nested dictionary ( dioictionary inside dictionary)

# student = {
#     "name" : "Harshal",
#     "marks" : {
#         "marathi" : 97,
#         "math" : 88,
#         "english" : 85
#     }
# }

# to print key from dict inside dict
# print(student["marks"]["english"])




# dictionary methods
"""
1. mydict.keys()   # return all keys
2. mydict.values()  # return all values
3. mydict.items()   # return all(key, val) pairs as tuples
4. mydict.get("key")  # return the kay according to values
5. mydict.update(newDict)  # insert the specific items to the dictionary

"""
# 1 key()

# student = {
#     "name" : "Harshal",
#     "marks" : {
#         "marathi" : 97,
#         "math" : 88,
#         "english" : 85
#     }
# }
# print(student.keys()) # output will show in list form
# print((list(student.keys())))   # for output in list form
# print(len(list(student.keys())))   # len of list

# print(len(student))  # for student  dict
# print(len(student["marks"]))  # for marks dict




# 2 values()

# student = {
#     "name" : "Harshal",
#     "marks" : {
#         "marathi" : 97,
#         "math" : 88,
#         "english" : 85
#     }
# }

# print(student.values())
# print(list(student.values()))





# 3 items


# student = {
#     "name" : "Harshal",
#     "marks" : {
#         "marathi" : 97,
#         "math" : 88,
#         "english" : 85
#     }
# }

# print(student.items())       # it will show items in perinthesis(key , value) means in tuple
# print(list(student.items()))

# pairs = list(student.items())      # to access indidualy key values
# print(pairs[0])



# 4   get("key")

# student = {
#     "name" : "Harshal",
#     "marks" : {
#         "marathi" : 97,
#         "math" : 88,
#         "english" : 85
#     }
# }

# print(student["name"])           # normal
# print(student.get("name"))       # method

# print(student["name1"])     # will give error
# print(student.get("name1")) # will give None



# 5 update(newDict)

student = {
    "name" : "Harshal",
    "marks" : {
        "marathi" : 97,
        "math" : 88,
        "english" : 85
    },
   "age" : 23
}

# student.update({"city" : "nagpur"})
# print(student)

# or 

# new_dict = {"city" : "Nagpur"}
# student.update(new_dict)
# print(student)


new_dict = {"age" : "Nagpur"}     # duplicate key passing, only update values with available key
student.update(new_dict)
print(student)