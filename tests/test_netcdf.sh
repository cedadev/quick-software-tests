#!/bin/sh

rm -f simple_xy.nc simple_xy_wr simple_xy_rd

gfortran simple_xy_wr.f -o simple_xy_wr -L$CONDA_PREFIX/lib -I$CONDA_PREFIX/include -lnetcdf -lnetcdff
if ! ./simple_xy_wr | grep -q SUCCESS
then
    echo "netcdf fortran example failed"
    exit 1
fi

gcc simple_xy_rd.c -o simple_xy_rd -L$CONDA_PREFIX/lib -I$CONDA_PREFIX/include -lnetcdf
if ! ./simple_xy_rd | grep -q SUCCESS
then
    echo "netcdf C example failed"
    exit 1
fi

int_var=$(ncdump -h simple_xy.nc  | perl -lne 'print $1 if /^\s+int (.*?)\(/')

if [ "$int_var" != "data" ]
then
    echo ncdump test fail
    exit 1
fi

rm -f simple_xy.nc simple_xy_wr simple_xy_rd

echo ran netcdf tests
exit 0
