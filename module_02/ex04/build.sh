#!/bin/bash

# Upgrade pip
# pip install --upgrade pip

# Build my_minipack package in wheel and egg format
# pip wheel . -w dist

python3 -m pip install --upgrade pip build setuptools wheel
python3 -m build

# You can then run the script by running the following command:
# ./build.sh
