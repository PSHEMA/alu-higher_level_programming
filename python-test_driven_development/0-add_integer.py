#!/usr/bin/python3
"""A function that adds twwo integers"""


def add_integer(a, b=98):
    """An addition function"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
