#!/bin/bash

script=write_netcdf.r
files="colornames.nc writevals.nc"

rm -f $files

if ! R -f $script
then
    echo "R failed"
    exit 1
fi

echo "verifying content"
for file in $files
do
    if [ ! -e $file ]
    then
	echo "$file not created"
	exit 1
    fi
    if ! diff -q -w ${file}dump <(ncdump $file)
    then
	echo "$file - not expected content"
	exit 1
    fi
done

echo "done"
