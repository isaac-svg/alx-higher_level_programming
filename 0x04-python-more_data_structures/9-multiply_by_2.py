#!/usr/bin/python3

def multiply_by_2(a_dictionary: dict):
    """Write a function that returns a new dictionary
      with all values multiplied by 2"""
    new_dic = {}
    for key, value in a_dictionary.items():
        new_dic[key] = value * 2
    return new_dic
