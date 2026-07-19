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


def check_disk_usage(disk):
    """Returns True if there is enough free disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    percent_free = (du.free / du.total) * 100
    return percent_free > 20  # Check if more than 20% free space

def check_cpu_usage():
    """Returns True if the CPU usage is below 75%, False otherwise."""
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent < 75  # Check if CPU usage is below 75%

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR! Not enough disk space or CPU usage is too high.")
else:
    print("Everything is OK.")