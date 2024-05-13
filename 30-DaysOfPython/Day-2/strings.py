# String is sequence of character 
# we use single or double quote to contian string
# multiple line string can be defined 
example = """dfjkdfafkdsfj adfkjsdf lkdf dfkajdlkdsr fksdfdjf ad;f
akjsd fadfkldfj; sdfaksdfjars;kj fdkf a
rushabh 
shdfsdf 
sdjfahsdfeuir dsfhaseuoe 
"""

print(example)

# Access string variables
# Python doesn't have character data type so single character is simple string with the length of one.

example = "s"
print(type(example))

# Accessing string characters
example = "rushabh is gonna master python."

print(example[1]) # indexing start fron 1 
print(example[11]) 

print(example[-5]) # Negative index start from -1

print(example[1:10]) # Slicing 

print(example[:10]) # from start to end point

print(example[4:]) # from start to end of the string

print(len(example)) #length of the string

print("rushabh" in example) # will return true or false

print("mahek" not in example) # will return true or false

# There are other string function go through it



