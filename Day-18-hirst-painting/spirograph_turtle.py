"""
Program: Spirograph
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle, Screen
from color_picker import get_random_color

screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.speed('fastest')
timmy.hideturtle()

for _ in range(72):
    timmy.color(get_random_color())
    timmy.circle(150)
    timmy.setheading(timmy.heading() + 5)

screen.exitonclick()
