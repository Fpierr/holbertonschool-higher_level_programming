#!/user/bin/python3
"""function that returns the JSON representation of an object (string)"""


import json
"""import the module"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
