#!/usr/bin/python3
"""Defines a Student  class."""


class Student:
    """Represent a student object."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str) -- The first name of the student.
            last_name (str) -- The last name of the student.
            age (int) -- The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student object.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list) -- (Optional) The attributes to represent.
        """
        if (type(attrs) is list and
                all(type(element) is str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
