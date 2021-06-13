from turtle import Turtle, Screen
from random import choice, randint

screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.pensize(10)
tim.speed(10)


def get_random_color():
    """returns a random rgb tuple"""
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def go_for_random_walk(turtle_obj):
    angle = [0, 90, 180, 270]
    turtle_obj.setheading(choice(angle))
    turtle_obj.forward(30)


for _ in range(200):
    colour = get_random_color()
    tim.color(colour)
    go_for_random_walk(tim)

screen.exitonclick()
