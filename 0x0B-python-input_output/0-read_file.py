#!/usr/bin/python3
"""Defines a function that reads a file
 and writes the content to stdout"""


def read_file(filename=""):
    """reads from a file and prints it to stdout"""
    with open(filename) as file:
        for f in file:
            print(f)
