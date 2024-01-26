#!/usr/bin/python3
"""Makes a GET request to github using their API"""

import sys
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = sys.argv[1]
    token = sys.argv[2]
    res = requests.get(url, auth=(username, token))
    jsonres = res.json()
    print(jsonres.get('id'))
