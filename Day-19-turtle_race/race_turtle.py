"""
Program: Turtle Race Program
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=800, height=400)
GAME_ON = False
user_bet = screen.textinput(title='Enter your bet',
                            prompt='Which turtle will win the race? '
                                   'red/green/blue/gray/pink/purple : ')
colors = ['red', 'green', 'blue', 'gray', 'pink', 'purple']
all_turtles = []

Y_AXIS = -150
for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-390, Y_AXIS)
    Y_AXIS += 60
    all_turtles.append(new_turtle)

if user_bet:
    GAME_ON = True

while GAME_ON:
    for turtle in all_turtles:
        if turtle.xcor() > 370:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color} has won the race.")
            else:
                print(f"You lost! {winning_color} has won the race.")
            GAME_ON = False
        else:
            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
