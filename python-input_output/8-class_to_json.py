#!/usr/bin/python3
"""returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """definition of function"""
    if hasattr(obj, "__dict__"):
        obj_dict = obj.__dict__.copy()

        for key, value in obj_dict.items():
            if isinstance(value, (list, dict, str, int, bool)):
                continue
            elif hasattr(value, "__dict__"):
                obj_dict[key] = class_tosjson(value)
            else:
                obj_dict[key] = str(value)

        return obj_dict
    else:
        raise TypeError(f"Ojbect of type {type(obj)} is not serializable.")
