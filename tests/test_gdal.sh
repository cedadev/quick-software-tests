#!/bin/sh

#
# test gdal - convert a tiff file to netcdf, with and without subsetting,
# and test the sizes
#
# Note: the input file has been subsetted from
# https://download.osgeo.org/geotiff/samples/gdal_eg/cea.tif
# using
# gdal_translate -projwin -28000 4228000 -26000 4226000 cea.tif gdal_test.tif

exedir=$(dirname $(which gdal_translate))
if [ "$exedir" != "$CONDA_PREFIX/bin" ]
then
    echo "gdal_translate not in conda environment?: $exedir"
    exit 1
fi

rm -f test1.nc test2.nc

gdal_translate gdal_test.tif test1.nc
gdal_translate -projwin -27500 4227500 -26500 4226500 gdal_test.tif test2.nc

ny1=$(gdalinfo test1.nc | awk '/Size is/{print $4}')
ny2=$(gdalinfo test2.nc | awk '/Size is/{print $4}')

echo $ny1 $ny2

rm -f test1.nc test2.nc

if [ $ny1 -eq 33 -a $ny2 -eq 17 ]
then
    echo "gdal test passed"
else
    echo "gdal test failed"
    exit 1
fi
