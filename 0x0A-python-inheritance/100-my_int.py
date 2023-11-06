#!/usr/bin/python3
"""Defines a class MyInt that inherits or extends from int."""


class MyInt(int):
    """Invert the != and == int operators"""

    def __eq__(self, value):
        """Override == opeartor with != operator."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == operator."""
        return self.real == value
