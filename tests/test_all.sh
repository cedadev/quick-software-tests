#!/bin/bash

DATA_SRC=root@jasmin-cylc.ceda.ac.uk:/home/users/ajh/cfplot_data
DATA_DIR=cfplot_data

if [ ! -d $DATA_DIR ]; then
    echo "[WARN] Copying example netcdf files to run tests."
    scp -r $DATA_DRC $DATA_DIR
fi

if [ ! -d $DATA_DIR ]; then
    echo "[ERROR] Cannot get example data so NOT running tests."
    exit
fi

source /appx/contrib/jaspy/miniconda_envs/jaspy3.7/m3-4.6.14/bin/activate jaspy3.7-m3-4.6.14-r20200226

python test_cfplot.py
