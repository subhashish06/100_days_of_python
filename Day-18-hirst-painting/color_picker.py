"""
Program: Color picker function
Author: Subhashish Dhar
Date: 03/09/2021
"""

from random import randint


def get_random_color():
    """returns a random rgb tuple"""
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    return red, green, blue
