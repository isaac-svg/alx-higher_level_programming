#!/usr/bin/python3
'''Defines a function that writes a text to a file'''


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
