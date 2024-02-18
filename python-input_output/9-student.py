#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance."""
        student_dict = {}
        for key in ['first_name', 'last_name', 'age']:
            value = getattr(self, key)
            if isinstance(value, (list, dict, str, int, bool)):
                student_dict[key] = value
            elif hasattr(value, "__dict__"):
                student_dict[key] = value.to_json()
            else:
                student_dict[key] = str(value)
        return student_dict
