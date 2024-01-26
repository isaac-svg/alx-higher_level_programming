#!/usr/bin/python3
"""Sends a request to the url passed as argv[1]"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.code}")
