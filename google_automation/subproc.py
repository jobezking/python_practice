#!/usr/bin/env python3

import subprocess
import os
from pathlib import Path

subprocess.run(["date"])
subprocess.run(["sleep", "2"])
result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stdout.decode().split())

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)
cwd_subprocess = subprocess.check_output(['pwd'], text=True).strip()
cwd_os = os.getcwd()

cwd_pathlib = Path.cwd()

subprocess.run(['mkdir', 'test_dir_subprocess2'])
os.mkdir('test_dir_os2')
test_dir_pathlib2 = Path('test_dir_pathlib2')