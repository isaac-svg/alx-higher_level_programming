#!/usr/bin/python3
"""Defines a function that appends to a file"""


def append_write(filename="", text=""):
    """Appends a text to a file"""
    with open(filename, "+a", encoding="utf-8") as file:
        return file.write(text)
