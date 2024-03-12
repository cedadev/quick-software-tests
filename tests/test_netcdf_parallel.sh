#!/bin/sh
#
# netCDF parallel test.
#
# Uses a modified version of the parallel test routines from 
# https://github.com/Unidata/netcdf-fortran/tree/main/examples/F90
# in which the output file path is specified on the command line,
# because the current directory might not be one that allows
# parallel access.
#

np=8

fc=$(nf-config --fc)
fflags=$(nf-config --fflags)
flibs=$(nf-config --flibs)

outdir=/work/scratch-pw2/$(id -un)/parallel-nc-test
if [ -d $outdir ] || mkdir -p $outdir
then
    echo "using directory $outdir"
else
    echo "$outdir does not exist (and cannot be created) using /tmp"
    outdir=/tmp
fi
ncfile=$outdir/simple_xy_par.nc
rm -f $ncfile
				   

for name in simple_xy_par_wr simple_xy_par_rd
do
    src=$name.F90
    obj=$name.o
    exe=./$name

    rm -f $obj $exe
    set -ex
    $fc $fflags -c -o $obj $src
    $fc -o $exe $obj $flibs
    set +ex

    if ! mpirun -n $np $exe $ncfile | grep -q SUCCESS
    then
	echo running $name failed
	exit 1
    fi
done

int_var=$(ncdump -h $ncfile  | perl -lne 'print $1 if /^\s+int (.*?)\(/')
if [ "$int_var" != "data" ]
then
    echo 'ncdump test fail (1)'
    exit 1
fi

x_size=$(ncdump -h $ncfile | perl -lne 'print $1 if /^\s+x = (.*?)\s*;/')
if [ "$x_size" -ne $np ]
then
    echo 'ncdump test fail (2)'
    exit 1
fi

#rm $ncfile

echo ran netcdf fortran parallel tests
exit 0
