#!/bin/sh

Rscript terra.r
if [ $? -ne 0 ]
then
    echo "R failed"
    exit 1
fi
