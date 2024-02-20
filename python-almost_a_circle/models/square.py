#!/usr/bin/python3
"""The class of square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """declaration of the class squre inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """inistalizing method of the class square constructor"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string that represente a square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
