#!/bin/bash

for i in `seq 1 $1`
do
    echo "Case $i"
    snakeviz ./stats/case$i.prof &
    echo
done