#!/usr/bin/python3
"""Defines a function that coverts a json string to
an object"""
import json


def from_json_string(my_str):
    """converts json to string"""
    return json.loads(my_str)
