#!/usr/bin/python3
"""Inherits from int"""


class MyInt(int):
    """A class that inherits from int and inverts == and != operators"""

    def __eq__(self, other):
        """Inverts == operator"""
        return int(self) != other

    def __ne__(self, other):
        """Inverts != operator"""
        return int(self) == other
