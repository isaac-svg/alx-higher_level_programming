#!/usr/bin/python3
"""Makes a post request with an email as a parameter"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    param = {'email': email}
    data = urllib.parse.urlencode(param)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
