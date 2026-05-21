##############################################
# # Note
##############################################
# Subscripting a list 
# when we consider string as a list of characters, we can use subscripting to get a specific character from the string
# e.g. "Hello"[0] will give us "H"
# 
# (1) Errors
# - ValueError:

## ++++++++++++++++++++++++++++++++++++++++++++
# print("Hello"[0]) # H
# print("Hello"[1]) # e
# print("Hello"[-1]) # o

# Data Types

# # string concatenation
# print("123" + "456") # 123456

# # Integer
# print(123 + 456) # 579

# print(123_456_789) # 123456789

# # Float
# print(3.14159) # 3.14159

# # Boolean
# print(True) # True
# print(False) # False

# print(type(123)) # <class 'int'>
# print(type(3.14159)) # <class 'float'>
# print(type("Hello")) # <class 'str'>
# print(type(True)) # <class 'bool'>

# # Type Casting
# print(str(123))
# print(int("123") + int("456"))

# print("Number of letters in your name: " + str(len(input("What is your name? "))))


# # Maths Operations
# print(3 + 5) # 8
# print(7 - 4) # 3
# print(3 * 2) # 6
# print(6 / 3) # 2.0 division, it will give us the result as a float (inplicit type conversion)
# print(2 ** 3) # 8  power, it will give us the result of 2 multiplied by itself 3 times (2 to the power of 3)
# print(5 % 2) # 1  modulus, it will give us the remainder
# print(8 // 3) # 2   integer division, it will give us the quotient without the remainder

# PEMDAS
# Parentheses
# Exponents
# Multiplication and Division (from left to right)
# Addition and Subtraction (from left to right)
# print(3 + 5 * 2) # 13
# print((3 + 5) * 2) # 16


# # Rounding
# print(int(8.7)) # 8 -- this is flooring, it will give us the largest integer less than or equal to the given number
# print(round(8.7)) # 9 -- this is rounding, it will give us the nearest integer to the given number
# print(round(3.14159, 2)) # 3.14 -- this is rounding to a specific number of decimal places

# # Manipulating value base on its current value
# age = 20
# age += 1 # age = age + 1
# print(age) # 21
# age -= 1 # age = age - 1
# print(age) # 20

# # f-string
# score = 0
# height = 1.8
# is_winning = True
# print(f"Your score is {score}, your height is {height}, and you are winning is {is_winning}")


# Tips Calculator

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_bill = bill * (1 + tip / 100)
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")