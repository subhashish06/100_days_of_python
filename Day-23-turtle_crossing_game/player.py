"""
Program: Turtle Crossing Player Module
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle

STARTING_POSITION = (0, -280)
PACE = 10


class Player(Turtle):
    """creates the player object"""
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.reset_position()
        self.setheading(90)

    def move(self):
        """moves the player forward"""
        self.forward(PACE)

    def reset_position(self):
        """resets the players position to start"""
        self.goto(STARTING_POSITION)
