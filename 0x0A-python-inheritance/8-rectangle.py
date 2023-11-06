#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Defines a class Rectangle that inherits from BaseGeometry."""


class Rectangle(BaseGeometry):
    """Extends the BaseGeometry class."""

    def __init__(self, width, height):
        """Intialize a new Rectangle object.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
