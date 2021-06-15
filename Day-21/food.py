from turtle import Turtle
from random import randint


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('blue')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.change_position()

    def change_position(self):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)
