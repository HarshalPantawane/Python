# string function

# str.endswith("er.")   # return  true if string ends with substr
 
# str.capitalize()      # capitalzes 1st char

# str.replace(old,new) #replace all occurrences of old with new

# str.find(WORD)  # returns 1st index of occurrer

# str.count("am")  # count the occurrence of substr 

#####################################

str = "abcde#fghijkl#nopqrs#tuvwxyz"

# print(str.endswith("apx"))
# print(str.capitalize())      # work only one time
# print(str.replace("#","@"))
# print(str.find("#"))           # it will give 1st index of that char / if not found prinnt -1
print(str.count("#"))
