#!/bin/bash

# Send a string to black and check it is fixed
resp=$(black -c "print ('hi')")

if [ $resp != 'print("hi")' ] ; then
    echo "[ERROR] Black failed."
    exit 1
else
    echo "[INFO] Black worked."
fi

