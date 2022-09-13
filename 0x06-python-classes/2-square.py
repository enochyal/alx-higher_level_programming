#!/usr/bin/python3
""" Module Square """


class Square:
    """ Square class defined by shape

        Attributes:
            size (ini): Size of square
    """
    def __init__(self, size=0):
        """
        Initialize methode

        Args:
            size (int): size of square
        """
        try:
            size = int(size)
        except TypeError:
            print("size must be an integer")
        try:
            size >= 0:
        except ValueError:
            print("size must be >= 0")

