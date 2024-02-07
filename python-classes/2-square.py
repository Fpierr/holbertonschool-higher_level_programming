#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        """Initialize a new Square instance with a given size.

        Args:
            size (int): The size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        # Private attibut to store the size
        self.__size = size
