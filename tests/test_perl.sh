#!/bin/sh

perldir=$(dirname $(which perl))
if [ "$perldir" != "$CONDA_PREFIX/bin" ]
then
    echo "no perl in environment?"
    exit 1
fi

answer=$(perl -e 'if ( 2 == 2 ) { print "foo\n" } else { print "bar\n" }')

if [ "$answer" == "foo" ]
then
    echo perl test worked
    exit 0
else
    echo perl test failed
    exit 1
fi
