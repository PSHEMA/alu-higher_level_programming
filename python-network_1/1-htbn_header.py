#!/usr/bin/python3
"""A python script that sends arequest to the URL and displays the value of the X-Request-ID"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.info()
        print(html.get('X-Request-Id'))
