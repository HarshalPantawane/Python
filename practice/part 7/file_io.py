"""
pythin can used to perform operations on a file.( read and write data)
type of files 

1. text file : .txt, .docs, .log, .etc

2. binary files: .mp4, .mov, .png, .jpng etc.

all file store in memory in form of bit 
"""

# operation on file.

# 1. Open, read and write file.
# we have to open a file before reading or writing.

# f = open("file_name", "mode")

# data = f.read

# f.close()

# read file

# f = open("demo.txt", "r") # for out of foleder, give full path
# data = f.read()
# print(data)
# print(type(data))
# f.close()

"""
there are diff file  mode
1. 'r' open for reading (default)
2. 'w' open for writing, trucating the file first(clear all data)
3. 'x' create a new file and open it for writing
4. 'a' open for writing , append to the end of the file if it exists
5. 'b' binary mode
6. 't' text mode(default)
7. '+' open a disk file for updating(reading and writing)
8. 'r+' read and write(replace with old ch) in starting of file
9. 'w+' write(truncate) and read  
"""


# for read some char
# f = open("demo.txt","r")

# data = f.read(6)        # read by char
# print(data)

# f.close()

# read by line
# f = open("demo.txt", "r")

# line1 = f.readline()
# print(line1)

# f.close()

# if you read whole file in once, in that case line read will show space( empty line). because whole file have already red.
# if you go lin by line, it will show

# # you can print any line from file
# f = open("demo.txt", "r")
# line = f.readlines()
# print(line[0])        

################################################################
# # write mode       # override file
# f = open("demo.txt", "w")
# f.write("i am writing new file")

# f.close()

# # append mode
# f = open("sample.txt", "a")     
# f.write("\nappend file and add content") # if you rum same file with same add contend, it will add multiple time
# f.close()

#### in write and append both mode, if file not exist, then file will create


# r+ mode

# f = open("sample.txt", "r+")
# f.write("abc")   # after overriding, pointer go to next char and will read from this.
# print(f.read())
# f.close()


# # w+
# f = open("demo.txt", "w+")
# print(f.read())            # file opened in truncated mode, nothing will print
# f.write("abc")

# f.close()

# a+ mode   read and append 

# f = open("demo.txt","a+")
# print(f.read())        # append meand end of 
# f.write("abc")
# f.close()



###########################
"""
with key word

with syntax

with open("demo.txt", "a) as f:
    data = f.read()
"""

# with open("sample.txt", "r") as f:     # it s work like function, no need to close
#     data = f.read()                    # all abuve line store in f
#     print(data)
    
# with open("sample.txt", "w+") as f:
#     f.write("new line")
    

# with open("sample.txt", "w") as f:     # f is file handler
#     file = "second latest new line"
#     f.write(file)
#     print(file)                      # give parameter to store output
   
   
# write new line and print whole file


# with open("sample.txt", "w+") as f:
#     f.write("line 1: hello world!\n")
#     f.write("line 2: python file handling\n")   
    
#     f.seek(0)            # reset cursor position to back to the start(index 0) 
    
#     content = f.read()
#     print(content)



# with open("sample.txt", "a+") as f:
#     f.write("line 1: hello world!\n")
#     f.write("line 2: python file handling\n")   
    
#     f.seek(0)            # reset cursor position to back to the start(index 0) 
    
#     content = f.read()
#     print(content)

# with open("sample.txt", "r+") as f:
#     f.write("line 1: hello harshal bhava\n")
#     f.write("line 2: python file checking\n") 
#     f.write("line 3: whole file print")  
    
#     f.seek(0)            # reset cursor position to back to the start(index 0) 
    
#     content = f.read()
#     print(content)



# with open("sample.txt", "r+") as f:    # 
#     f.write("line 1: ndshsadfujoe\n")
   
    
#     f.seek(0)            # reset cursor position to back to the start(index 0) 
    
#     content = f.read()
#     print(content)

##################################################################
"""
deleting a file

using the "os" module  # this is pre installed
module (like a code lib) is a file written by another progremmer that generally has a function we can use.

  import os    
  os.remove(filename)
  
"""
# for delete file 

# import os
# os.remove("sample.txt")

#########################################################3
# practice
# 1. create a new file "practice.txt" using python. add the following data in it: 
# Hi everyone
# we are learning file i/o
# using java.
# i like programming in python 

# 1st way

# f = open("practice.txt","w")
# f.write("hi everyone\n")
# f.write("we are leaaring file i/o\n")
# f.write("using python\n")
# f.write("i like programming in python\n")

# f.close()

# 
# import os
# os.remove("practice.txt")

## 2nd way
# with open("practice.txt","w") as f:
#     f = open("practice.txt","w")
#     f.write("hi everyone\nwe are leaaring file i/o\n")
#     f.write("using python\ni like programming in python\n")



# 2. WAF that replace occurrences of "Java",with "python" in aboe file.
# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("python", "java")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)

# 3. search if the word "learing" exeist in the file or not.
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if(data.find("learing") >= 0):
#         print("found")
#     else:
#         print("not fount")
        
# in function 

# def check_word():
#     with open("practice.txt", "r") as f:
#        data = f.read()
#        if(data.find("learing") >= 0):
#            print("found")
#        else:
#            print("not fount")
       
# check_word()           

# 4. WAF to find in which line of the file does the word "learning" occure first.print-1 if not fount

# def check_word():
#   word = "learning"
#   with open("practice.txt","r") as f:
#     data = f.read()
#     if(word in data):
#       print("found")
#     else:
#       print("not found")  

# def check_for_line():
#   word = "learning" 
#   data = True 
#   line_no = 1
#   with open("practice.txt", "r") as f:
#       while data:
#         data = f.readline()
#         if(word in data):
#           print(line_no)
#           return
#         line_no += 1  
#   return -1 

# print(check_for_line())

# 5. from a file containing numbers separated by comma, print the count of even numbers.


# with open("demo.txt", "r") as f:
#   data = f.read()                 # Data is in string format
#   print(data)
#   # print(type(data))
  
#   num = ""
#   for i in range(len(data)):
#     if(data[i] == ","):
#       print(int(num))
#       num = ""
#     else:
#       num += data[i]
      
# # or 
count = 0
with open("demo.txt", "r") as f:
  data = f.read()      
  
  num = data.split(",")      #a string method used to break a single string into a list of smaller strings based on a specific separator (delimiter).
  for val in num:
    if(int(val) % 2 == 0):
      count += 1
      
print(count)