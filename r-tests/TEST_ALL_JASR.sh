#!/bin/bash

if [ ! $(which R) ]; then
    echo "[ERROR] Please activate the JasR environment before running tests."
    exit 1
fi

cd $(dirname $0)
. ../tests/_funcs
make_logdir


if [ ! -d cfplot_data ]
then
    ln -s /home/users/ajh/cfplot_data/ .
fi
 
export PLOT_DIR=../compare/images/test
mkdir -p $PLOT_DIR

# test all python
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
