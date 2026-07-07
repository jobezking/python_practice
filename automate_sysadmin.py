#!/usr/bin/env python3

import shutil
import psutil

du = shutil.disk_usage("/")
print("Total: %d GiB" % (du.total / (2**30)))
print("Used: %d GiB" % (du.used / (2**30)))
print("Free: %d GiB" % (du.free / (2**30))) 
percent_free = (du.free / du.total) * 100
print("Percentage Free: %.2f%%" % percent_free)

cpu_percent = psutil.cpu_percent(interval=1) # interval is in seconds

for i in range(5):
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")