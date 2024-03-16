# It's flow statemetn
#  Suppose condition match then go and run that partucular block of code or else it will check anothr condition.abs
    # E.g    If condition :
    #           block of code
# Suppose that condition match it goes and enter the block of code

# Suppose you have to check condition if it doesn't match go for default logic. 

# If-else
    #       if condition :
    #           Block1 of code
    #       else condition :
    #           Block2 of code

# If-elif-else
    # E.g   if condition :
    #           Block1 of code
    #       elif condition :
    #           Block2 of code
    #       else :
    #           Default Logic


a = int(input("Enter value of a : "))
b = int(input("Enter the value of b: "))

if a == b:
    print("A , B are same")
else:
    print("A and B are differnt")

if a > b:
    print("A is greater then b")
elif b > a:
    print("B is greater then a")
else:
    print("Both are same")



