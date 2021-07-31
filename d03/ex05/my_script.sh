#!/bin/sh

python3 -m venv Django
source Django/bin/activate
pip install --force-reinstall -r requirement.txt
