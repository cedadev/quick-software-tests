#!/bin/bash

if [ ! $(which conda) ]; then
    echo "[ERROR] Please activate the Conda/Jaspy environment before running tests."
    exit
fi
 
export PLOT_DIR=../compare/images/test
mkdir -p $PLOT_DIR

export DATA_DIR=$(python -c 'import os, iris_sample_data as isd; sample_data_dir = os.path.join(os.path.dirname(isd.__file__), "sample_data"); print(sample_data_dir)')


#DATA_SRC=root@jasmin-cylc.ceda.ac.uk:/home/users/ajh/cfplot_data
#DATA_DIR=cfplot_data

#if [ ! -d $DATA_DIR ]; then
#    echo "[WARN] Copying example netcdf files to run tests."
#    scp -r $DATA_DRC $DATA_DIR
#fi

if [ ! -d $DATA_DIR ]; then
    echo "[ERROR] Cannot get example data so NOT running tests."
    exit
fi

#python test_cfplot.py
cmd="R -f test.R"
$cmd

if [ ! $? ]; then
    echo "[ERROR] Failed: $cmd"
    exit
fi 

cmd="python test_cartopy.py"
$cmd

if [ ! $? ]; then
    echo "[ERROR] Failed: $cmd"
    exit
fi



