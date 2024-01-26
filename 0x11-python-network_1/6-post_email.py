#!/usr/bin/python3
"""Makes a post request to an email address"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    response = requests.post(url, data=values)
    print(response.text)
