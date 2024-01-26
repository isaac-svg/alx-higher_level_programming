#!/usr/bin/python3
"""Makes a post request to the url"""

import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        data = sys.argv[1]
    else:
        data = ""
    payload = {'q': data}
    response = requests.post(url, data=payload)
    try:
        jsonres = response.json()
        if jsonres:
            print(f"[{jsonres.get('id')}] {jsonres.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
