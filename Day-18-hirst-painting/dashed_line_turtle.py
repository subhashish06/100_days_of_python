"""
Program: Dashed Line Program
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen.exitonclick()
