#!/usr/bin/python3

def best_score(a_dictionary: dict):
    """Write a function that returns a key with
    the biggest integer value."""

    if not a_dictionary:
        return None
    largest = 0
    largestKey = ''
    seen = False
    for key, value in a_dictionary.items():
        if not seen:
            largest = value
            seen = True
        if value > largest:
            largestKey = key
            largest = value
    return largestKey
