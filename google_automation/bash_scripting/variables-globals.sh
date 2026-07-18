example=hello
echo $example

#!/bin/bash

line="-------------------------------------------------"

echo "Starting at: $(date)"; echo $line

echo "UPTIME"; uptime; echo $line

echo "FREE"; free; echo $line

echo "WHO"; who; echo $line

echo "Finishing at: $(date)"

./gather-information.sh 

echo *.py
echo c*
echo *
echo ?????.py
Code output:

areas.py hello.py