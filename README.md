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