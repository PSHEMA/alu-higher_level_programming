#!/usr/bin/python3
"""A function that adds a new attribute to an object"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if it's possible"""
    if hasattr(obj, '__dict__'):
        obj.__dict__[attr] = value
    else:
        raise TypeError("can't add new attribute")
