#!/bin/sh

value=$(udunits2 -H "2m/s" -W "km/h"  | head -n 1 | awk '{print $4}')

if [ "$value" = "7.2" ]
then
    echo "udunits2 test passed"
    exit 0
else
    echo "udunits2 test failed"
    exit 1
fi
