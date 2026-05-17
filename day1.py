##############################################
# # Note
##############################################
# (0) PEP8: 
#  - has one empty line at the end of file
#
# (1) Errors
# - SyntaxError
# - IndentationError
#
# (2) String Concatenation
#
# (3) Built-in Function: input()
#
# (4) Variable
# name = input("What is your name? ")
#
# (5) Buit-in Function for string
# - len()
# 
# (6) Naming Your Variables
# - snake_case
# - meaningful name

## ++++++++++++++++++++++++++++++++++++++++++++

# print("Hello World!\nHello World!\nHello World!")

# string concatenation
# print("Hello" + " " + "Angela")

# print(" ".join(["Hello", input("What is your name? "), "!"]))
# print("Hello " + input("What is your name? ") + "!")

## ++++++++++++++++++++++++++++++++++++++++++++

# # variable
# name = input("What is your name? ")
# print("Hello " + name + "!")

# length_of_name = len(name)
# print(length_of_name)

## ++++++++++++++++++++++++++++++++++++++++++++

print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + city + " " + pet)