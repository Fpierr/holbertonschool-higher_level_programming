#!/usr/bin/python3
"""Write the first class Base"""

import json


class Base:
    """the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """define init method"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string representation."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []

        # Get the class name
        class_name = cls.__name__

        # create the filename
        filename = "{}.json".format(class_name)

        # Convert list_objs to a list of dictionaries
        list_dicts = [obj.to_dictionary() for obj in list_objs]

        # Convert the list of dictionaries to JSON string
        json_str = cls.to_json_string(list_dicts)

        # write the JSON string to the file
        with open(filename, "w") as file:
            file.write(json_str)
