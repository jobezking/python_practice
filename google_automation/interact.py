#!/user/bin/env python3

#cat hello.py

name = input("Please enter name: ")
print(f"Hello, {name}!")

def to_seconds(hrs, mins, secs):
    return hrs * 3600 + mins * 60 + secs

continue_program = "y"
while continue_program.lower() == "y":
    try:
        hours = int(input("Enter hours: "))
        minutes = int(input("Enter minutes: "))
        seconds = int(input("Enter seconds: "))
        
        total_seconds = to_seconds(hours, minutes, seconds)
        print(f"Total time in seconds: {total_seconds}")
    except ValueError:
        print("Please enter valid integers for hours, minutes, and seconds.")
    
    continue_program = input("Do you want to continue? (y/n): ")

print("Farewell! Thank you for using the program.")

# echo $PATH
# /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
# cat variables.py
#!/usr/bin/env python3
import os
print("HOME: " + os.environ.get("HOME", ""))
print("SHELL: " + os.environ.get("SHELL", ""))
print("FRUIT: " + os.environ.get("FRUIT", ""))

# ./variables.py 
# export FRUIT=Pineapple
#./variables.py

# cat parameters.py 
#!/usr/bin/env python3
import sys
print(sys.argv)

# ./parameters.py
#['./parameters.py'] 

#./parameters.py one two three
#['./parameters.py', 'one', 'two', 'three']


# wc variables.py
#7 19 174 variables.py 	
#echo $?
#0

#wc notpresent.sh
#wc: notpresent.sh: No such file or directory
#echo $?
#1

#!/usr/bin/env python3

import os
import sys

filename = sys.argv[1]

if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("This is a new file created by the script.\n")
    print(f"File '{filename}' created.")
else:
    print(f"File '{filename}' already exists.")
    sys.exit