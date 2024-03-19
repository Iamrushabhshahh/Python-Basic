# For loop run the loop till all the desired value is hit.

for i in range(10):
    print(i)


# Also in loop we use staement to control flow 
# Break : This will break the flow when certain condition got matched
# Continue : This will continue the flow when certain condition is matched.abs

print('============= Break Example ====================')

for i in range(5):
    if(i == 3):
        break # This will be break and flow end
    print(i)

print('============= Continue Example ====================')

for i in range(5):
    if(i == 3):
        continue #This will be skipped   
    print(i)


# if/else allow us to conditionally run code
# while allow us to repitatively run code as long as condition true
# for in loop run in sequence till condition sataisfy.