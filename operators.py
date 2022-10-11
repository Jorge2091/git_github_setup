# Let's see the operators in action
# Intro to Data types & Operators
# - `+ - * /`

# Comparison Operators
# - `<` less than
# - `>` greater than
# - `==` True or False
# - `>=` greater than or equal
# - `<=` less than or equal

# a=24
# b=16
#
# print(a+b) # outcome added value of a & b
# print(a-b) # outcome subtracted b from a

# comparison
# print(a >b) # True
# print(a<b) # False
# print(a == b) # False

# % operator - find out what it is how it's used in python
# create a print statement to show the use case of it

# % is the reminder when you divide a number from another number

# c = 3
# d = 10
#
# print(d%c) # this will give a reminder of 1

# != means not equal, it is the opposite of "=="

# Boolean Builtin methods in Python - Boolean Methods
# DRY do not repeat yourself print("")
# greeting = "Hello World!"
# print(greeting) # show text written
# print(greeting.isalpha()) # sees if it is letters only
# print(greeting.islower()) # checks if all are upper
# print(greeting.startswith("H")) # checks if starts with a H
# print(greeting.endswith("!")) # checks if it ends with a !
# print(greeting.isdigit()) # check if it is a digit

# string Slicing
# string indexing - starts from 0
# H  e  l  l  o      W   o  r   l   d   !
# 0  1  2  3  4  5   6  7   8   9   10  11
#              -2 -1

# greeting = "Hello World!"
# print(greeting)
# # we have a builtin method that checks the length of string
# print(len(greeting)) # checks the length of text
# print(greeting[0]) # will select the first letter
# print(greeting[-12:-6])
# print(greeting[-6:])

# String Methods are available
# use var = string "asfdsfaasdfsadfsadf                  "
# white_space = "lots of spaces at the end                 "
# print(len(white_space))
# # Strip() removes the white spaces
# print(len(white_space.strip()))
# example_text = "here's sOme text wIth lOt's of text"
# print(example_text.count("text"))
# print(example_text.lower()) # makes all text in string is lower case
# print(example_text.capitalize())
# print(example_text.replace(" wIth",","))

# User data input
# first_name = "Jorge"
# last_name = "Reyes"
# salary = 40
# print(first_name)
# print(last_name)
# print(first_name + last_name)
# print(first_name + " " + last_name)

# print(first_name + " " + last_name + str(salary)) # cast int to string using str()
#
# # F-string
# print("hello {} {}".format(first_name, salary))
first_name = input("What is your first name?")
last_name = input("What is your last name? ")
UK_resident = input("Are you a UK resident? YES or NO  ")
house_number = input("What is your house number? ")
street_name = input("What is the street name of your house? ")
postcode = input("What is the postcode of your house? ")
DOB = input("What is your date of birth in the format ddmmyy ")
course_name = input("What is the course you are taking? ")
first_name = first_name.lower()
first_name = first_name.capitalize()
last_name = last_name.lower()
last_name = last_name.capitalize()

print("Hello {} {}.".format(first_name, last_name))
print("You are a UK resident living in {} {}".format(house_number, street_name))
print(postcode)
print("Your date of birth is {} and you are undertaking the {} course in Sparta Global".format(DOB, course_name))
