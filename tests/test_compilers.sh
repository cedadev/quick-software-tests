#!/bin/bash

# compile a "hello world" program with Fortran, C and C++

obj=./test.exe
output=test.out

status=0

while read compiler source
do
    echo "Compiling and running $source using $compiler"
    rm -f $obj $output
    $compiler -o $obj $source && $obj >& $output
    if [ $status -ne 0 ]
    then
	echo "** Failed to compile and/or run"
	status=1
    else
	cat $output
	if [ $(cat $output) != hello ]      
	then
	    echo "** Unexpected program output"
	    status=1
	fi
    fi
done <<EOF
gfortran hello.f
gcc hello.c
g++ hello.cpp
EOF
