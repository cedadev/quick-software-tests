#!/bin/bash

all_out=all_imports_output.$$
this_out=$all_out.this
err_out=all_imports_output_where_failed.$$

rm -f $all_out $this_out $err_out

cat libraries | while read lib
do
    echo "=== $lib ===" > $this_out

    echo "library($lib)" | R --no-save >> $this_out 2>&1
    status=$?

    if [ $status -eq 0 ]
    then
	echo "$lib: success"
    else
	echo "$lib: FAIL"
	cat $this_out >> $err_out
    fi
    cat $this_out >> $all_out
done
rm -f $this_out

echo "for full output see $all_out"

if [ -e $err_out ]
then
    echo "***** THERE WAS ONE OR MORE FAILURE *****"
    echo "for error output see $err_out"
    exit 1
else
    echo "No failures"
fi

