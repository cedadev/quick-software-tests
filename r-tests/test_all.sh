#!/bin/bash

if [ ! $(which conda) ]; then
    echo "[ERROR] Please activate the Conda/Jaspy environment before running tests."
    exit
fi

if [ ! -d cfplot_data ]
then
    ln -s /home/users/ajh/cfplot_data/ .
fi
 
export PLOT_DIR=../compare/images/test
mkdir -p $PLOT_DIR

function test_run {

    cmd=$1
    echo "[INFO] Running test: $cmd"
    $cmd

    if [ $? -eq 0 ]
    then
	echo "Success: $cmd" | tee -a succeeded
    else
        echo "[ERROR] Failed: $cmd" | tee -a failed
    fi
}

rm -f succeeded failed
# 
# test all python
for fn in test*.py
do
    test_run "python $fn"
done

# test all sh
for fn in test*.sh
do
    if [ $fn != `basename $0` ]
    then
	test_run ./$fn
    fi
done

# commented out general loop over R programs - R programs are run via shell scripts
# # test all R
# for fn in test*.R
# do
#     test_run "R -f $fn"
# done


