"""
set is the collection of the unodered items.
Each element in the set must be unique and immutable.
"""
# collection = {5,3,7,2,5,3,4,4,"Harshal",6.0}     # duplicate values will not print
# print(collection)
# print(type(collection))

# print(len(collection))  # duplicate items will ignored


######### empty set  ########

# collections = {}  # if you wil give this, this is empty dict

# # for empty set
# collections = set()  
# print(type(collections))

"""
set methods
1. set.add(el)  # adds an element

2. set.remove() # remove the elem en 

3. set.clear()  # empties the set

4. set.pop()    # remove a random value

5. set.union(set2)   # combines both set values and return new.

6. set.intersections(set2)    # combines common values and returns new
"""
# set is mutable but set element is immutable.

# 1 set.add()
# collection = set()
 
# collection.add("Harshal")            # you can add immutable, but not add mutable like lis and dict
# collection.add(1)
# collection.add(2.0)
# collection.add(0)
# collection.add([1,2,3,4,5])

# print(type(collection))
# print(collection)



# # 2 set.remove
# collection = {5,3,7,2,5,3,4,4,"Harshal",6.0}

# collection.remove(5)  # all duplicate are remove
# print(collection)


# # 3 set.clear
# collection = {5,3,7,2,5,3,4,4,"Harshal",6.0}

# collection.clear()           # will give set()
# print(collection)
# print(len(collection))       # output is 0


# 4 set.pop
# collection = {5,3,7,2,5,3,4,4,"Harshal",6.0}


# print(collection.pop())         # will give any random value from set
# print(collection.pop()) 


# 5 set.union(set2)   combine both set and return new set, common from both used single


# collections1 = {1,2,3,4,5,6,"Harshal",7.0}
# collections2 = {11,2,12,13,3,14,15}

# collections = collections1.union(collections2)
# print(collections)



# 6 set.intersection

collections1 = {1,2,3,4,5,6,"Harshal",7.0}      
collections2 = {11,2,12,13,3,14,15}

colllection = collections1.intersection(collections2)    # print common value from both
print(colllection)