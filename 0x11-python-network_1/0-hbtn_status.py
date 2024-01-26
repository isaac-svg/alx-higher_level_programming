#!/usr/bin/python3
"""Makes a fetch request to a url"""
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        res = response.read()
        print("Body response:")
        print(f"\t- type: {type(res)}")
        print(f"\t- content: {res}")
        print(f"\t- utf8 content: {res.decode('utf-8')}")
