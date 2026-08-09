# 1 store following word meqnings in a python dictionary:
    # cat : a small animal,
    # table : a piece of furniture, list of facts and figures

# dict = {
#     "cat" : "a small animal",
#     "table" : ["a piece of furniture", "list of facts and figures"]
# }

# print(dict)


# 2 you have given of subject for student.Assume one classroom is required for 1 subject. how many classroons are needed by all students.
# "pyhton", "java", "c++", "python", "javascript", "c"

# subjects = {"python", "java","c++","c","javascript","pyhton","c++","java"}

# classroom = subjects

# print("classrooms needed: ",len(classroom))



# 3 WAp to enter marks of 3 subject from the user and store them in a dictionary. start with an 
# empty dictionary and add one by one. use subject name as key and marks as value


# subjects = {}

# sub = {
#     "marathi" : 12,
#     "english" : 15,
#     "math" : 15
# }
# subjects.update(sub)

# print(subjects)

# # or 

# marks = {}

# x = int(input("Enter mark of math: "))
# marks.update({"math" : x})
# y = int(input("Enter mark of chem: "))
# marks.update({"chem" : y})
# z = int(input("Enter mark of phy: "))
# marks.update({"phy" : z})

# print(marks)


# 4 figure out a way to store 9 and 9.0 as separate values in the set. 
# (you can take help of built-in data type)

# 1 option
# num = {9, "9.0"}
# print(num)

# 2 option
value = {
    ("float", 9.0),
    ("int", 9)
}
print(value)