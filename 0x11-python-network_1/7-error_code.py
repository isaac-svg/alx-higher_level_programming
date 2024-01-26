#!/usr/bin/python3
"""Prints the reponse if the Status Code 
of the response is less than 400"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    try:
        print(res.text)
        if res.status_code >= 400:
            raise requests.exceptions.HTTPError
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(res.status_code))
