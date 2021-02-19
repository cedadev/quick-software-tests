#!/bin/bash

rm -f h5ex_d_fillval h5ex_d_fillval.h5

gfortran -o h5ex_d_fillval  h5ex_d_fillval.f90 -L$CONDA_PREFIX/lib -I$CONDA_PREFIX/include -lhdf5_fortran

if ! diff -q <(./h5ex_d_fillval) h5ex_d_fillval.expected_output
then
    echo "hdf5 example failed"
    exit 1
fi

rm -f h5ex_d_fillval h5ex_d_fillval.h5

echo ran hdf5 tests
exit 0
