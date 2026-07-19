#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1], 'r') as file:
    lines = file.readlines()
    for line in file:
        oldvalue = line.strip()
        newvalue = oldvalue.replace("jane", "jdoe")
        subprocess.run(["mv", oldvalue, newvalue])
file.close()