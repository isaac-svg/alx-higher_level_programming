#!/usr/bin/python3
"""Defines a function that reads a file
 and writes the content"""


def read_file(filename=""):
    """reads from a file and prints"""
    with open(filename, "r") as file:
        for f in file:
            print(f)
