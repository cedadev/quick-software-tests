#!/bin/sh

out=out.nc
rm $out

# ask for two variables from one of the cfplot test data files (contains 3 vars)
# and see how many float variables we got in the output file

cdo -select,name=longitude,latitude testdata/orca2.nc $out

nfloat=$(ncdump -h $out | grep -c float)

rm $out

if [ "$nfloat" = "2" ]
then
    echo "cdo test passed"
    exit 0
else
    echo "cdo test failed"
    exit 1
fi
