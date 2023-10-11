#!/usr/bin/python3

def complex_delete(a_dictionary: dict, needle):
    for key, value in a_dictionary.copy().items():
        if needle == value:
            del a_dictionary[key]
    return a_dictionary
