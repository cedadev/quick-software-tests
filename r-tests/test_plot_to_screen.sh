#!/bin/sh

echo 'source("plot_to_screen.r")' | R --interactive --no-save
if [ $? -ne 0 ]
then
    echo "R failed"
    exit 1
fi

echo -n "Did that display a plot? "
while true
do
    read answer
    case $answer in
	[Yy]*)
	    echo "returning success"
	    exit 0
	    ;;
	[Nn]*)
	    echo "returning failure"
	    exit 1
	    ;;
    esac
done
