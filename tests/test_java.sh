#!/bin/bash

# compile a "hello world" program with Java

compiler=javac
source=hw.java
obj=HelloWorld
objfile=$obj.class
output=test.out

# check that it is getting the compiler from CONDA_PREFIX
for cmd in java javac
do
    cmd_path=$(which $cmd)
    if [ "$(dirname $cmd_path)" != "$CONDA_PREFIX/bin" ]
    then
	echo "** $cmd is at $cmd_path, not in conda env bin dir"
	exit 1
    fi
done	   

echo "Compiling and running $source using $compiler"
rm -f $objfile $output
javac $source && java $obj >& $output
status=$?
if [ $status -ne 0 ]
then
    echo "** Failed to compile and/or run"
    exit 1
else
    cat $output
    if [ "$(cat $output)" != "hello" ]      
    then
	echo "** Unexpected program output"
	exit 1
    fi
fi
