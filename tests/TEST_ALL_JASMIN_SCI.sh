#!/bin/bash

cd $(dirname $0)
. _funcs

make_logdir

# test all sh
for fn in $(cat jasmin_sci_tests)
do
    if is_excluded $fn
    then
	echo "skipping excluded test: $fn"
	continue
    fi

    test_run $fn
done

summarise_and_exit
