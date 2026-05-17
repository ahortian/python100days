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


## ++++++++++++++++++++++++++++++++++++++++++++

# print(
# """
# 1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.
# 2. Knead the dough for 10 minutes.
# 3. Add 3g of Salt.
# 4. Leave to rise for 2 hours.
# 5. Bake at 200 degrees C for 30 minutes.
# """
# )

# print("Hello World!\nHello World!\nHello World!")

# string concatenation
# print("Hello" + " " + "Angela")

print("".join(["Hello ", input("What is your name? "), "!"]))
print("Hello " + input("What is your name? ") + "!")