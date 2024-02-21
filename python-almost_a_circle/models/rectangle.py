#!/usr/bin/python3
"""the rectangle classe inherits from base class"""


from models.base import Base


class Rectangle(Base):
    """the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """define method init to initialize the rectangle"""

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Calculate the area of the rectangle"""
        return self.width * self.height

    def __str__(self):
        """Return a string that representing the class rectanhle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def display(self):
        """Print # to display the rectangle considering x and y"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """update attribute of the rectangle instance with key"""
        attributes = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, attributes[i], args[i])
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns a dictionary representation of the Rectangle.

        Returns:
            dict: A dictionary containing the attributes of the Rectangle.
                Keys:
                    - 'id' (int): The identifier of the Rectangle.
                    - 'width' (int): The width of the Rectangle.
                    - 'height' (int): The height of the Rectangle.
                    - 'x' (int): The x-coordinate of the Rectangle.
                    - 'y' (int): The y-coordinate of the Rectangle.
        """
        return {
            'x': self.x,
            'y': self.y,
            'id': self.id,
            'height': self.height,
            'width': self.width,
        }

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0 or value == 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0 or value == 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getty for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
