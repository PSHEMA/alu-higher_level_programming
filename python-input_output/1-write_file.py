#!/usr/bin/python3
"""A function that writes a string to a text file"""


def write_file(filename="", text=""):
    """A function"""
    with open(filename, 'w+') as f:
        return f.write(text)
