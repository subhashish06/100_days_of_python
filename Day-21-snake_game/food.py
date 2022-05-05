"""
Program: Snake Food Module
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle
from random import randint


class Food(Turtle):
    """The Food Class."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.change_position()

    def change_position(self):
        """randomly changes the food position on screen"""
        x_value = randint(-280, 280)
        y_value = randint(-280, 280)
        self.goto(x_value, y_value)
