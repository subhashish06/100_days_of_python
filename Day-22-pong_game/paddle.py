"""
Program: Ping Pong Paddle Module
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle


class Paddle(Turtle):
    """creates the paddle object"""
    def __init__(self, x_cor=0, y_cor=0):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(x=x_cor, y=y_cor)

    def move_up(self):
        """moves the paddle up the screen"""
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def move_down(self):
        """moves the paddle down the screen"""
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
