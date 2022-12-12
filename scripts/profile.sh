#!/bin/bash

for i in `seq 1 $1`
do
    echo "Case $i"
    python -m cProfile -o ./stats/case$i.prof -s tottime ./case$i.py
    echo
done