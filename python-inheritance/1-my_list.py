#!/usr/bin/python3
"""My list"""


class Mylist(list):
    """My list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
