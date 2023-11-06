#!/usr/bin/python3
"""Defines a function that writes attributes to objects."""


def add_attribute(obj, attribute, val):
    """Add a new attribute to an object if writable.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute.
        val (any): The value of att parameter.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, val)
