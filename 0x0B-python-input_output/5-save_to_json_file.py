#!/usr/bin/python3
"""Defines a function that writes an object to a file as string"""
import json


def save_to_json_file(my_obj, filename):
    """writes python object to a file as string"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
