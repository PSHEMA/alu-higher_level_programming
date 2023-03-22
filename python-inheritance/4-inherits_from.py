#!/usr/bin/python3
"""T or F"""


def inherits_from(obj, a_class):
    """T or F"""
    if type(obj) == a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
