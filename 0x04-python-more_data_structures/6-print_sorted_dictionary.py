#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Write a function that prints a dictionary
      by ordered keys."""
    sortedKeys = sorted(a_dictionary)
    for key in sortedKeys:
        print("{}: {}".format(key, a_dictionary[key]))
        