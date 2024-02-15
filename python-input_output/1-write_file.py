#!/usr/bin/python3
"""Defines a function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """Writes a string to a text file (UTF8) and returns the number of char...
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
