#!/bin/sh

Rscript terra-netcdf.r
if [ $? -ne 0 ]
then
    echo "terra netCDF test failed"
    exit 1
fi
