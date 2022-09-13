#!/usr/bin/python3
""" Module Square """

class Square:
    """ Sauare class is defined by shape

        Attrbute:
            size (int): int to assign to square size
    """
    def __init__(self, size=0):
        """
        Initilize method

        Args:
            size (int): int to assign to square size
        Raises:
            TypeError: if size is not int
            ValueError: size less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
