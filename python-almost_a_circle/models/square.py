#!/usr/bin/python3
"""The class of square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """declaration of the class squre inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """inistalizing method of the class square constructor"""

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string that represente a square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)
