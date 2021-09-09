"""
Program: Draw Shape with Turtle
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle, Screen
from random import choice

screen = Screen()
tim = Turtle()
colours = ['red', 'blue', 'green', 'yellow', 'orange', 'violet', 'pink', 'gray']
SIDES = 3


def draw_shape(number_of_sides):
    """draws the shape"""
    angle = 360
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle/number_of_sides)


for side in range(SIDES, 11):
    tim.color(choice(colours))
    draw_shape(side)


screen.exitonclick()
