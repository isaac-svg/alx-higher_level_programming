#!/usr/bin/python3
"""Makes a GET request to Github for commits made on a repo"""

import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".\
            format(sys.argv[2], sys.argv[1])
    res = requests.get(url)
    jsres = res.json()
    for key, v in enumerate(jsres):
        if key == 10:
            break
        print("{}: {}".format(v.get('sha'),
                              v.get('commit').get('author').get('name')))
