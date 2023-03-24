#!/usr/bin/python3
"""A function that appendsa string at the end of a text file"""


def append_write(filename="", text=""):
    """The function"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
