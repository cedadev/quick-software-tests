#!/bin/sh

exe=./_test_blas

rm -f $exe
gfortran _test_blas.f -L$CONDA_PREFIX/lib -lblas -o $exe
output=$($exe)
rm -f $exe

if [ $output -eq 10 ]
then
    echo "blas test worked"
    exit 0
fi

echo "blas test failed"
exit 1

