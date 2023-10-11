#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Write a function that replaces all occurrences
    of an element by another in a new list."""

    return list(map(lambda x: x if (x != search) else replace, my_list))
