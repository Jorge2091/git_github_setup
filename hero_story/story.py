story1 = {
    "start": "I have been struggling with a code",
    "middle": "and I was running out of time",
    "end": "I searched the internet and W3School came to my rescue, my hero!!"
}
print(story1)
print(type(story1))
print(story1.keys())
print(story1.values())
print(story1["start"])
print(story1["middle"])
print(story1["end"])
story1["hero"] = "W3School"
print(story1)