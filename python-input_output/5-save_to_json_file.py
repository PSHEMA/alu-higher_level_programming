#!/usr/bin/python3
"""A function that writes an Object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """The function"""
    with open(filename, "w", encoding="utf8") as file:
        json.dump(my_obj, file)
