# input Promts the user to input some data from the console.
# It accepts an optional parameter that can be used in order to write a message before the user input.
# Always returns the string. 
# A program that doesn't use any input function, is called deaf program.

input("Enter your Surname : ")

# To make this thing useful and use it in programm we can assign variable to store input

Name=input("Enter you Name : ")
print("Your name is : " + Name)


# Input always returns the string so in cases of we need to take input in the integer or float we have to type cast

Age=int(input("Enter the Age : "))

print(Age - 5)
 
# For float

salary=float(input("What is your salry : "))
print(salary + 5000)
