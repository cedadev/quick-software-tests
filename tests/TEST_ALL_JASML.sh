#!/bin/bash

cd $(dirname $0)
. _funcs

make_logdir

if [ ! $(which conda) ]; then
    echo "[ERROR] Please activate the Conda/JasML environment before running tests."
    exit 1
fi

for fn in $(cat jasml_tests)
do
    test_run $fn
done
    
(summarise_and_exit)
status=$?

cat <<EOF
===============================================
This has only done the *extra* tests for JasML.

You should probably also run TEST_ALL_JASPY.sh
===============================================
EOF

exit $status
