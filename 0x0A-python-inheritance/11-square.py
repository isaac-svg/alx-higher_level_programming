#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""
Rectangle = __import__('9-rectangle').Rectangle


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
