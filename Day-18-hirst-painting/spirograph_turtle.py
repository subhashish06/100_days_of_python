from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.speed('fastest')
tim.hideturtle()


def get_random_color():
    """returns a random rgb tuple"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


for _ in range(72):
    tim.color(get_random_color())
    tim.circle(150)
    tim.setheading(tim.heading() + 5)

screen.exitonclick()
