#!/bin/bash

out=$((echo foo ; echo bar) | parallel -k ./_test_parallel_helper.sh 2>/dev/null | fmt -80)

if [ "$out" = "oof rab" ]
then
    echo parallel test passed
    exit 0
else
    echo parallel test failed
    exit 1
fi

