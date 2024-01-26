#!/usr/bin/python3
"""Makes a send request to the url from argv[1]"""

import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as res:
        print(res.getheader("X-Request-id"))
