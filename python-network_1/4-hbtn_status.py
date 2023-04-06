#!/usr/bin/python3
"""A Python script that fetches https://alu-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    t = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
