#!/bin/bash

files=$(ls)

for f in $files 
do
    if [ -f "$f/.env" ]; then
        cp "$f/.env" "${f}_env.txt"
    fi
done