#!/usr/bin/python3
"""A python script that sends a request and displays the the value of the X-Request-Id"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except:
        pass
