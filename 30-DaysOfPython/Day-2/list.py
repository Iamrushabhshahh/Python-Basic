# List is collection of multiple item in single variable / like an array 

mylist = ['a' , 'b', 'c', 'd', 'e', 'f']

print(mylist)

# list item
    # are ordered, changable and allow duplicates
    # llist item are indexed idex start from [0]

#  lIST ITEM CAN BE OF ANY DATA TYPES
#  list has it's own data type called list

print(type(mylist))

# Length function is used to find the number of item in list

# Working with list item ( element )

# Access list elements using index value
 
print(mylist[2])

# list slicing

print(mylist[1:4])

# Add more element to list 

mylist.append("g")
print(mylist)
 
# extends list

myist1 = [1, 2, 3, 4, 4, 5]
myist1.extend(mylist)
print(myist1)

# Inser / based on index value

myist1.insert(5,7)
print(myist1)


#  Change element in a list using assignment operator
myist1[4] = 100
print(myist1)


# Remove element from list

# Using delete statement 
del myist1[4]
print(myist1)
# remove using remove method

myist1.remove(4)
print(myist1)