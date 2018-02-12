# Lists and List Comprehensions

print("Francis Parker".lower())

name = "Francis Parker"

for char in name:
    print(char.lower(), char)

my_list = ["Bev", "Abe", "Cam", "Dan", "Eve", "Flo", "Gus"]
my_numlist = [8, 4, 7, 5, 2, 9]

# using indices
print(my_list[3])
my_list[3] = "Deb"
print(my_list)

# slicing
print(my_list[3:5]) # prints index 3 and 4
print(my_list[:4]) # from beginning to 3
print(my_list[4:]) # from 4 to the end
print(my_list[:]) # prints whole list

# copying a list
my_list_copy = my_list # NOT THIS WAY
my_list_copy[-1] = "Gob" # can use negative indices
print(my_list_copy)
print(my_list)

my_list_copy = my_list[:] # this copies the whole list into a new one
my_list_copy[-2] = "Feb" # can use negative indices
print(my_list_copy)
print(my_list)

# Methods for Lists and Functions
print( "Deb" in my_list) # checks if this is in the list, prints True or False

# Find the min and max of a list
print(min(my_numlist))
print(max(my_numlist))
print(sum(my_numlist))
print(min(my_list)) # Alphabetical (sort of) goes by ordinal order
# print(ord("A"))

# find the index
print(my_list.index("Deb"))

# find how many times an item appears in a list
print(my_list.count("Gob"))

# add to a list
my_list.append("Gob")
print(my_list.count("Gob"))

# insert a value into a list
my_list.insert(3, "Don")
print(my_list)

# sort a list
print(my_list)
my_list.sort()
print(my_list) # sorts according to the ordinal

# Reverse the list
my_list.reverse()
print(my_list)

# clear a list
my_list.clear()
print(my_list)

my_list = my_list_copy[:]

# POP - removes an item from the list and returns it
print(my_list)
remove_name = my_list.pop()
print(my_list)
print(remove_name)

first_name = my_list.pop(0) # you can put the index in there
print(first_name)
print(my_list)

# Delete an item from a list
del my_list[0]
print(my_list)
del my_list[1:3]
print(my_list)

# Iterating
# For each loop - cannot change the list within this method
for item in my_numlist:
    item *= 2
    print(item)

print(my_numlist)

# Index variable loop
for i in range(len(my_numlist)):
    my_numlist[i] *= 2
    print(my_numlist[i])

print(my_numlist)

# CREATING LISTS
# Make a list of number 1 to 100
my_list = []
for i in range(1, 101):
    my_list.append(i)

print(my_list)

# Go back through the list and square everything
for i in range(len(my_list)):
    my_list[i] **= 2
    print(my_list[i])

print(my_list)

