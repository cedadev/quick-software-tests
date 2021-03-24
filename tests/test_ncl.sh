#!/bin/sh

tar xvfz england_gor_2011.tar.gz

ncl _test_ncl.ncl &
pid=$!

sleep 1

echo "Opening plot... "

while true
do
    echo -n "does plot contain the outline of London? "
    read ans
    case $ans in
	[Yy]*)
	    echo "NCL test succeeded"
	    status=0
	    break
	    ;;
	[Nn]*)
	    echo "NCL test failed"
	    status=1
	    break
	    ;;
    esac
done

kill $pid
sleep 1
if [ -e /proc/$pid ]; then kill -9 $pid; fi

rm -f england_gor_2011.{dbf,prj,shp,shx}
exit $status
