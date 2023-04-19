#!/bin/sh

env=/tmp/testenv.$$
vn=0.0.4

rm -fr $env

python3 -m venv --system-site-packages $env

. $env/bin/activate

if [ $(which pip) != $env/bin/pip ]
then
    echo virtualenv failed
    exit 1
fi

pip install hello-world-python==$vn

version=$(pip freeze | perl -lne 'print $1 if /hello-world-python==(.*)/')

message=$(python -c 'from hello_world import hello_world; print(hello_world.hello_world("jaspy"))')

rm -fr $env

if [ "$version" = "$vn" -a "$message" = "Hello World jaspy" ]
then
    echo "virtualenv / pip test passed"
    exit 0
else
    echo "virtualenv / pip test failed"
    exit 1
fi


