import os

file = open("spider.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()
with open("spider.txt") as file:
    print(file.readline())

with open("spider.txt") as file:
    for line in file:
        print(line.upper())

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)

f = open("sample_data/declaration.txt", "w")
f = open('workfile', 'w', encoding="utf-8") 

with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

with open("novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

#CWD command for external files:
outputs['current_directory_before'] = os.getcwd()
    
"""
The mode argument is optional, and it specifies the mode in which the file is opened. If omitted, it defaults to ”r” and that means opening for reading in text mode. The common modes include:

"r"  open for reading (default)

"w" open for writing, truncating the file first

"x"  open for exclusive creation, failing if the file already exists

"a"  open for writing, appending to the end of the file if it exists

"+"  open for both reading and writing
"""