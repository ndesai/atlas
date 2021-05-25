#!/usr/bin/env bash

PYTHONPATH+=$PWD/thirdparty/qface:
PYTHONPATH+=$PWD/../atlas-genpack-htmldoc:
PYTHONPATH+=$PWD/../atlas-genpack-cpp:

PYTHONPATH=$PYTHONPATH \
    ./gen.py \
    --interface-path=interfaces
