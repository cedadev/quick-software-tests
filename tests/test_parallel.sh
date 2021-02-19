#!/bin/bash

out=$((echo foo ; echo bar) | parallel ./_test_parallel_helper.sh 2>/dev/null)

if [ "$out" = "oof rab" ]
then
    echo parallel test passed
    exit 0
else
    echo parallel test passed
    exit 1
fi

