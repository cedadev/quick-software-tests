#!/bin/bash

if [ ! $(which conda) ]; then
    echo "[ERROR] Please activate the Conda/Jaspy environment before running tests."
    exit
fi
 
export PLOT_DIR=../compare/images/test
mkdir -p $PLOT_DIR

export DATA_DIR=$(python -c 'import os, iris_sample_data as isd; sample_data_dir = os.path.join(os.path.dirname(isd.__file__), "sample_data"); print(sample_data_dir)')


if [ ! -d $DATA_DIR ]; then
    echo "[ERROR] Cannot get example data so NOT running tests."
    exit
fi

#python test_cfplot.py

function test_run {

    cmd=$1
    echo "[INFO] Running test: $cmd"
    $cmd

    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed: $cmd"
        exit
    fi

}

test_run "python test_pymc3.py"
test_run "R -f test.R"
test_run "python test_cartopy.py"
test_run "./test_black.sh"
test_run "python test_tabulate.py"
test_run "python test_llvmlite.py"

