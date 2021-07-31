#!/bin/sh

virtualenv --python=python3 django_venv; source django_venv/bin/activate
pip -V
pip install --force-reinstall -r requirement.txt