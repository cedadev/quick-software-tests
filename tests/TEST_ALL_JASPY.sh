#!/bin/bash

cd $(dirname $0)
. _funcs

make_logdir
exclude_files="jasmin_sci_tests $exclude_files"

if [ ! $(which conda) ]; then
    echo "[ERROR] Please activate the Conda/Jaspy environment before running tests."
    exit 1
fi

export PLOT_DIR=../compare/images/test
mkdir -p $PLOT_DIR

export DATA_DIR=$(python -c 'import os, iris_sample_data as isd; sample_data_dir = os.path.join(os.path.dirname(isd.__file__), "sample_data"); print(sample_data_dir)')

if [ ! -d $DATA_DIR ]; then
    echo "[ERROR] Cannot get example data so NOT running tests."
    exit 1
fi

for fn in test*.py test*.sh
do
    if is_excluded $fn
    then
	echo "skipping excluded test: $fn"
	continue
    fi
    test_run $fn
done
    

summarise_and_exit
