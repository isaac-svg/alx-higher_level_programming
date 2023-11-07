#!/usr/bin/python3
"""Defines a function for converting an object to string"""
import json


def to_json_string(my_obj):
    """Converts json string to object"""
    return json.dumps(my_obj)
