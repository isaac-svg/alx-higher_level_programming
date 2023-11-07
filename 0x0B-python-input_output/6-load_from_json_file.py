#!/usr/bin/python3
"""Defines a function that coverts a JSON file to an object"""
import json


def load_from_json_file(filename):
    return json.load(filename)
