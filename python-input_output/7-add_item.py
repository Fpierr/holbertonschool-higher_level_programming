#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file"""

import sys
from os import path
from json import dump, load
from importlib import import_module

filename = "add_item.json"

# Check if the file exists
if path.exists(filename):
    # If the file exists, load the existing list
    with open(filename, 'r') as file:
        my_list = load(file)
else:
    # If the file doesn't exist, create an empty list
    my_list = []

# Add the arguments to the list
my_list.extend(sys.argv[1:])

# Save the updated list to the file
with open(filename, 'w') as file:
    dump(my_list, file)
