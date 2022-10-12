# What is a dictionary - Data Collection type
# How to manage Dictionaries - How to manage the data using Dict
# It works as a key value pair; key = value
# syntax {"key": "value"}

# print(name[1])
# store student's data - name, course_name, progress, completed_lessons
student_1 = {
    "key": "value",
    "name": "Jorge",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lessons_names": ["list", "tuples", "strings"]
}
print(type(student_1))
print(student_1["stream"]) # This will display the value saved inside stream

student_1["completed_lessons"] = 3

# print/display completed_lessons_names


print(student_1["completed_lessons_names"])
print(student_1["completed_lessons_names"][0])

print(student_1)
# Delete an item from the list of completed_lessons_names
student_1["completed_lessons_names"].remove("strings")
print(student_1["completed_lessons_names"])
# Dict Builtin Methods
# display keys only or values
# keys() values()
print(student_1.keys())

# display values only from student_1
print(student_1.values())
