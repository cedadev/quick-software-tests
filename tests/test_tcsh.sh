#!/bin/sh

answer=$(tcsh -f -c 'if ( 2 == 2 ) echo foo; if ( 1 == 2 ) echo bar')

if [ "$answer" == "foo" ]
then
    echo tcsh test worked
    exit 0
else
    echo tcsh test failed
    exit 1
fi
