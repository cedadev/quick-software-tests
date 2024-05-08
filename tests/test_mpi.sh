#!/bin/sh

for progname in mpicc mpif90 mpirun
do
    exedir=$(dirname $(which $progname))
    if [ "$exedir" != "$CONDA_PREFIX/bin" ]
    then
	echo "$progname not in conda environment?: $exedir"
	exit 1
    fi
done

cexe=./mpi_send_recv_c
fexe=./mpi_send_recv_f
nproc=4

csrc=$cexe.c
fsrc=$fexe.f

rm -f $cexe $fexe
echo "compiling"
mpicc -o $cexe $csrc
mpif90 -o $fexe $fsrc
ls -l $cexe $fexe

for exe in $cexe $fexe
do

    echo "testing: $exe on $nproc procs"
    nproc_succ=$(mpirun -np $nproc $exe | awk '/SUCCESS FOR NPROC =/{print $5}')

    if [ -z "$nproc_succ" ]
    then
	echo "Failed"
	exit 1
    fi

    if [ $nproc_succ -ne $nproc ]
    then
	echo "Ran on wrong number of processors ($nproc_succ != $nproc)"
	exit 1
    fi

done

rm -f $cexe $fexe

echo "openmpi test succeeded"
