#!/bin/bash

# antonio maulucci 2023

# make environment
python3 -m venv venv

# activate environment
source venv/bin/activate

# install requirements
pip3 install -r requirements.txt

# run
# ./venv/bin/python3 -m src.main
#
# pyton3 -m src.main
#

# deactivate environment
deactivate

