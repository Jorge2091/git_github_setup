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
# print/display completed_lessons_names


print(student_1["completed_lessons_names"])
print(student_1["completed_lessons_names"][0])