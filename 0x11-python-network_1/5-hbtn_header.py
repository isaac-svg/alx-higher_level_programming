#!/usr/bin/python3
"""Gets a header info from a request"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    print(res.headers.get('X-Request-id'))
