"""
Program: Etch a Sketch
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    """moves the turtle forward"""
    tim.forward(10)


def move_backward():
    """moves the turtle backward"""
    tim.forward(-10)


def move_clockwise():
    """changes the turtle direction clockwise"""
    tim.right(5)


def move_counter_clockwise():
    """changes the turtle direction counter clockwise"""
    tim.left(5)


def clear_drawing():
    """clears the screen and resets the turtle position"""
    tim.clear()
    tim.reset()


screen.listen()
screen.onkeypress(fun=move_forward, key='Up')
screen.onkeypress(fun=move_backward, key='Down')
screen.onkeypress(fun=move_clockwise, key='Right')
screen.onkeypress(fun=move_counter_clockwise, key='Left')
screen.onkey(fun=clear_drawing, key='c')

screen.exitonclick()
