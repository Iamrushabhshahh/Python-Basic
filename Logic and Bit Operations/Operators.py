# When we want to check multiple condition then we use this kind og solution
# If you want to check two condition and both should match then it can be like.abs
# Also there's conditon for not
age = 30
gender = 'Male'

if( age >= 18 and gender == 'Female' ) :
    print("Conditon Matched")
else:
    print("Condition is not matching in And")

if( age >= 18 or gender == 'Female' ) :
    print("Or working")
else:
    print("Or isn't working")

if(not age == 20 ):
    print("It's getting true as age == 20 false")
elif(not age==30):
    print("It's False as age == 30 is true")
else:
    print("Give more attention for the not")
# Not just do Opposite of true ! if conditon true it makes it false, If condtion false it makes it true.