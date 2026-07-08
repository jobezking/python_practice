import os
import datetime

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

print(os.getcwd())
os.mkdir("new_dir")
os.remove("novel.txt")
os.chdir("new_dir")
os.mkdir("newer_dir")
os.rmdir("newer_dir")
os.listdir("website")

dir = "website"
for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

os.rename("first_draft.txt", "finished_masterpiece.txt")
os.path.exists("finished_masterpiece.txt")
os.path.getsize("spider.txt")
os.path.getmtime("spider.txt")
os.path.abspath("spider.txt")

timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp)

"""
The mode argument is optional, and it specifies the mode in which the file is opened. If omitted, it defaults to ”r” and that means opening for reading in text mode. The common modes include:

"r"  open for reading (default)

"w" open for writing, truncating the file first

"x"  open for exclusive creation, failing if the file already exists

"a"  open for writing, appending to the end of the file if it exists

"+"  open for both reading and writing
"""