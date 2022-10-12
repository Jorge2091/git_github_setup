# Dictionary Basics

### What are dictionary

Dictionary is a data type, it is used to store data values with corresponding keys. One example is shown below:
```python
person_1 = {
    "name": "jorge",
    "fav_colour": "purple",
    "fav_car": "volkswagen",
    "fav_number": 27
}
```
### Making a Hero Story!

We will create a short story and split it into 3 section; `start`, `middle` and `end`. <br/>
My story will be: <p style=" color: rgb(0, 255, 0);">I have been struggling with a code, and I was running out of time, I searched the internet and W3School came to my rescue, my HERO!!</p><br/>
I can put this into a section and save it in a dictionary, this can be seen below:
```python
story1 = {
    "start": "I have been struggling with a code",
    "middle": "and I was running out of time",
    "end": "I searched the internet and W3School came to my rescue, my hero!!"
}
```
We can print this dictionary the same way as other data types with the print fuction as shown below:
```python
print(story1)
```
we can print the type of data using the type function `print(type(story1))` <br/>
Another function available inside python is the keys only or value only. This will only print out the keys or values of a dictionary `print(story1.keys())` <br/>
To print out individual lines, you can call the call them out using the keys as shown below:
```python
print(story1["start"])
print(story1["middle"])
print(story1["end"])
```
It is also possible to add new keys using by calling a new name and its corresponding value, as shown below:
```python
story1["hero"] = "W3School"
```
To see if the value is added into the dictionary, we can use `print(story1)`
