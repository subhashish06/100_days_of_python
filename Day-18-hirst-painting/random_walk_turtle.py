"""
Program: Random Walk Program
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle, Screen
from random import choice
from color_picker import get_random_color

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.pensize(10)
tim.speed(10)


def go_for_random_walk(turtle_obj):
    """takes the turtle for a random walk"""
    angle = [0, 90, 180, 270]
    turtle_obj.setheading(choice(angle))
    turtle_obj.forward(30)


for _ in range(100):
    colour = get_random_color()
    tim.color(colour)
    go_for_random_walk(tim)

screen.exitonclick()
