from turtle import Turtle, Screen
from random import choice

screen = Screen()
tim = Turtle()
colours = ['red', 'blue', 'green', 'yellow', 'orange', 'violet', 'pink', 'gray']
sides = 3


def draw_shape(number_of_sides):
    angle = 360
    for _ in range(number_of_sides):
        tim.forward(100)
        tim.right(angle/number_of_sides)


for side in range(sides, 11):
    tim.color(choice(colours))
    draw_shape(side)


screen.exitonclick()
