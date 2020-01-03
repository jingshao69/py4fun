#!/bin/bash

while [ "$1" != "" ]; 
do
    echo "$1..."
    perl -pi -e 's/\r\n/\n/g' $1    
    shift 1
done

