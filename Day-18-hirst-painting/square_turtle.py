"""
Program: Draw Square
Author: Subhashish Dhar
Date: 03/09/2021
"""

# Look for colors : https://cs111.wellesley.edu/labs/lab01/colors

from turtle import Turtle, Screen

my_screen = Screen()
my_screen.bgcolor("cornsilk2")

timmy = Turtle()
timmy.color("cyan3")

for _ in range(4):
    timmy.forward(100)
    timmy.left(90)

my_screen.exitonclick()
