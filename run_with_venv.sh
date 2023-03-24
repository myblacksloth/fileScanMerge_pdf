#!/bin/bash

# ask for first file
echo "Enter the first file's path:"
read first_file

# ask for the second file
echo "Enter the second file's path:"
read second_file

# ask for the output directory
echo "Enter the output directory's path:"
output_file="output_$(date +'%Y-%m-%d_%H-%M-%S').pdf"
read dest_dir

# activate the environment
source venv/bin/activate

# execute command (merge)
python3 -m src.main -fa "$first_file" -fb "$second_file" -out "$dest_dir/$output_file"

# deactivate environment
deactivate
