#!/usr/bin/python3


def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True if the typeof a_class is an obj type.
        Otherwise - False.
    """
    if type(obj) is a_class:
        return True
    return False
