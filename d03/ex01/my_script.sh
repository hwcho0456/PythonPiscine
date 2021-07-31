#!/bin/sh

virtualenv --python=python3 local_lib; source local_lib/bin/activate
pip -V
pip install git+https://github.com/jaraco/path.git --force-reinstall --log path_install.log
python my_program.py