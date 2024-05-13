# three types of number

a = 5

print(type(a))

b = 5.5

print(type(b))

c = 10+20j

print(type(c))


# Type convertion have two type 
    #  1 ) Implicit - Wehn we add int and float output will be float that's implicit type conversition
x = a + b
print(type(x))

    #  2 ) Explicit - when we do type converetion using built in function ( i.e int(), float(), complex() ) that called explicit

# rushabh_age = int(input("Enter age \t"))

# print(type(rushabh_age))

# Random module : - that offer to generate the random number or pick random item from an iterator

import random

print(random.randint(1,10))

print(random.randrange(1,100))

print(random.random())