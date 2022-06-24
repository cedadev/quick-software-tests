#!/bin/sh

#
#  NCO test is essentially the same as the CDO test, but using ncks to do the
#  extraction instead of cdo
#

. ./_enable_scl

out=nco_out.nc
rm $out

# ask for two variables from one of the test data files (contains 3 vars)
# and see how many float variables we got in the output file

ncks -v longitude,latitude testdata/orca2.nc $out

nfloat=$(ncdump -h $out | grep -c float)

ncdump -h $out
rm $out

if [ "$nfloat" = "2" ]
then
    echo "nco test passed"
    exit 0
else
    echo "nco test failed"
    exit 1
fi
