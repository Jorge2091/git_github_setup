# Python Intro
## why python
- easy to use
- human readable
- high in demand

```python
# testing the env with print statement

# Python variables?
# To store any data -
# To store user data - hard code the data - any other type
# first_name = "Angel" - string
# name = "Subhaan"
# DOB = 99 - Int
# Uk_resident = yes or no - Boolean
# salary = 40000 - Int
# Travel = 15.4 - float
# gross_salary = salary + travel

first_name = "Jorge"
last_name = "Reyes"
salary = 50
travel = 3.3

# print("Jorge")
# print(first_name)
# print(last_name)
# print(salary)
# print(travel)

# how to find out the type of data stored in the var
# type()
# print(type(last_name))

# interact with users by taking user data in - input()
print("Good Morning, Please Enter your first Name")
first_name = input() # took user input & stored in the car called name
last_name = input("Now please input your last name: ")
print("Hello dear " + first_name + " " + last_name)
DOB = input("what is your date of birth in format ddmmyy:")
course_name = input("what is the course you taking")
UK_resident = input("are you a UK resident? YES or NO")
```

### Intro to Data types & Operators
- `+ - * /`

##### Comparison Operators
- `<` less than
- `>` greater than
- `==` True or False
- `>=` greater than or equal 
- `<=` less than or equal

```python
a=24
b=16

print(a+b) # outcome added value of a & b
print(a-b) # outcome subtracted b from a

# comparison
print(a >b) # True
print(a<b) # False
print(a == b) # False
```
```python

# % is the reminder when you divide a number from another number

# c = 3
# d = 10
#
# print(d%c) # this will give a reminder of 1

# != means not equal, it is the opposite of "=="

# Boolean Builtin methods in Python - Boolean Methods
# DRY do not repeat yourself print("")
greeting = "Hello World!"
print(greeting) # show text written
print(greeting.isalpha()) # sees if it is letters only
print(greeting.islower()) # checks if all are upper
print(greeting.startswith("H")) # checks if starts with a H
print(greeting.endswith("!")) # checks if it ends with a !
print(greeting.isdigit()) # check if it is a digit

# string Slicing
# string indexing - starts from 0
# H  e  l  l  o      W   o  r   l   d   !
# 0  1  2  3  4  5   6  7   8   9   10  11
#              -2 -1

greeting = "Hello World!"
print(greeting)
# we have a builtin method that checks the length of string
print(len(greeting)) # checks the length of text
print(greeting[0]) # will select the first letter
print(greeting[-12:-6])
print(greeting[-6:])

# String Methods are available
# use var = string "asfdsfaasdfsadfsadf                  "
white_space = "lots of spaces at the end                 "
print(len(white_space))
# Strip() removes the white spaces
print(len(white_space.strip()))
example_text = "here's sOme text wIth lOt's of text"
print(example_text.count("text"))
print(example_text.lower()) # makes all text in string is lower case
print(example_text.capitalize())
print(example_text.replace(" wIth",","))
```