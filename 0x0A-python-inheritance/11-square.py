#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Defines a Rectangle class that inherits from BaseGeometry."""


class Square(Rectangle):
    """Represent a square object."""

    def __init__(self, size):
        """Initialize a new square object.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size