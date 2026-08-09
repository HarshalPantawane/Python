# 1 WAp to ask the user to enter names of their 3 favourite movies and store them in a list.
# movies = []       # empty list is also valid

# mov1  = input("Enter 1 favourite movies name: ")
# mov2  = input("Enter 2 favourite movies name: ")
# mov3  = input("Enter 3 favourite movies name: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# or 

# movies = []

# mov = input("Enter 1st movie: ")
# movies.append(mov)
# mov = input("Enter 2st movie: ")
# movies.append(mov)
# mov = input("Enter 2st movie: ")
# movies.append(mov)

# print(movies)


# # or
# movies = []

# movies.append(input("Enter 1st movie: "))
# movies.append(input("Enter 2st movie: "))
# movies.append(input("Enter 3st movie: "))

# print(movies)




# 2 WAp to check if a  list is contains a palindrome of element.( Hint use copy()method)
# palindrome means "saas" ,"maam"

# list= [1,2,3]

# copy_list = list.copy()
# copy_list.reverse()

# if(copy_list == list): 
#     print("palindrome")
# else:
#     print("non palindrone")    
    
# 
# list= ["m","a","a","m"]

# copy_list = list.copy()
# copy_list.reverse()

# if(copy_list == list): 
#     print("palindrome")
# else:
#     print("non palindrone")        
    
    
# 3 WAp to count the number of student with the "A" grade in the following tuple.
# ("c","d","a","a","b","b","a") 

# tup = ("c","d","a","a","b","b","a") 

# print(tup.count("a"))



# 4 store the above values in a list and sort them from "a" to "d"
grade = ["c","d","a","a","b","b","a"]

grade.sort()
print(grade)