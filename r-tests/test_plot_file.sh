#!/bin/sh

plot=plot.png
script=plot_to_file.r

rm -f $plot

if ! R -f $script
then
    echo "R failed"
    exit 1
fi

if [ ! -e $plot ]
then
    echo "plot not created"
    exit 1
fi

display $plot &

echo "display of $plot has been launched (may take time to appear)"
echo -n "Has this made a plot? "
while true
do
    read answer
    case $answer in
	[Yy]*)
	    echo "please close the plot"
	    exit 0
	    ;;
	[Nn]*)
	    echo "returning failure"
	    exit 1
	    ;;
    esac
done
