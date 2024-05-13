"""================================ Operators in Python ============================================= 
 Author : Rushabh Shah
 E-mail : rushabhshah842@gmail.com
================================================================================================="""


# Arithmatic

a = 10 
b = 2

print ( "Here a is", a, "B is", b)
print("Addition ", a+b)

print("Substraction", a-b)

print("multiplication", a*b)

print("division", a/b) 

print("Modulo", a%b) # This gives remainder as return

print("Exponential", a**b) # Power

print("Floor Division", a//b) # This give quotient


# Assignment

c=50  # This is called assignment operator

print( "Value of C is here", c)

c += 5
print("c is",c)

c/=5
print("c is",c)

c**=4
print("c is",c)

c-=3
print("c is",c)

c %= 4
print("c is",c)

c *= 2
print("c is",c)



# Comparison 

d = 10
e = 5

print(d == e) # Equal to

print(d > e) # greater 

print(d < e) # less 

print(d >= e) # greater equal

print(d <= e) # less equal

print(d != e) # not

# Logical 

f = 40
g = 50

print( f and g )

print( f or g )

print(not f )

# Bit-Wise

#  This operators works on operand as if they were strings of binary digits



# Special
    # Identity 
        # In python "is" and "is not" are used to check if two values are located at the same part of memory
        # two variable that are equal doesn't imply that they are identical

x = False

if x is True:
    print("X",x)
elif x is not True:
    print("X is ",x)

     # Membership

# example of "in" and "not in" 

for i in range(40,50):
    if i % 2 == 0:
        print(i)
    


# Concatination is refered by the '+'



rushabh = 5 
mahek = 20 
 
print(rushabh + mahek) # 25

print( "Value of rushabh is", rushabh, "and mahek is", mahek, "Total is", rushabh+mahek) #Value of rushabh is 5 and mahek is 20 Total is 25

print ("Hey"+" Makdi")

print (True + rushabh)

print (False + mahek)


#  Print function 

print("Hey I'm print function")

# print ( object= separator= end= file= flush= )
    # Object  - value to be printed 
    # sep - allow us to separate multiple object using define separator 
print("Mahek anna rula sena sena kena ken agina ab aba cus", "ddahgasdgj ajsdhd g ba ba ba ", "sdfadsjfaha gjasg dgj", sep='$$##$$')

    # end - allows us to add specific value like \t \n 
print("Mahek", "ka", end='\n' "Mek motu error na aaveclear")

