# There are threee types of control statemtnt 
    # Conditional 
        # If, If-else, If-elif-else 
a = 5
b = 10

if a == 5:
    print(a)
else:
    print(b)

if a == 10:
    print(a)
elif b == 15:
    print(b)
else:
    print("enter valid value")



    ##      Iterative 
        # While, For

for i in range(10):
    print(i)

while a != 10:
    print(a)
    a += 1

    ###         Jumping
        # Break, Continue, pass

for i in range (10,50):
    if i == 15:
        break
    print(i)

print ("\n\n\n\n\n")

for i in range (10,50):
    if i%2 == 0:
        continue
    print(i)

for i in range (10,50):
    if i%2 == 0:
        continue
        pass # this is random placeholder to spoof compiler and skip it even it doens't contain any code.
    print(i)

