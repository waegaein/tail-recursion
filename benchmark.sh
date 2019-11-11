#!/usr/bin/env bash

if [[ "${#}" != "1" ]];
then
    printf "You need to provide one positional argument; number\n"
    exit 1
fi

python main.py 0 "${1}"
python main.py 1 "${1}"
python main.py 2 "${1}"
