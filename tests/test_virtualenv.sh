#!/bin/sh

env=/tmp/testenv
vn=0.2

rm -fr $env

virtualenv --system-site-packages $env

. $env/bin/activate

if [ $(which pip) != $env/bin/pip ]
then
    echo virtualenv failed
    exit 1
fi

pip install hello-world==$vn

version=$(pip freeze | perl -lne 'print $1 if /hello-world==(.*)/')

deactivate

rm -fr $env

if [ "$version" = "$vn" ]
then
    echo "virtualenv / pip test passed"
    exit 0
else
    echo "virtualenv / pip test failed"
    exit 1
fi


