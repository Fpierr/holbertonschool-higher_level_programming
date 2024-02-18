#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict

    def __repr__(self):
        """Return a string representation of the object."""
        return "Student({}, {}, {})".format(self.first_name,
                                            self.last_name, self.age)
