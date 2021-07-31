#!/bin/sh

python3 -m venv local_lib
source local_lib/bin/activate
python -m pip -V
python -m pip install git+"https://github.com/jaraco/path.git" --force-reinstall --log install.log
python my_program.py

