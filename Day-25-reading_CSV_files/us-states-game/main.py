"""
Program: US States Game
Author: Subhashish Dhar
Date: 03/09/2021
"""
# pylint: disable=no-member

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

data = pd.read_csv("50_states.csv")
states = data["state"].to_list()

guessed_states = []
while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 states guessed",
                                   prompt="What's the name of state?")
    user_answer = user_answer.title()
    if user_answer == 'Exit':
        missed_states = [state for state in states if state not in guessed_states]
        df = pd.DataFrame(missed_states)
        df.to_csv("states_to_learn.csv")
        break
    if user_answer in states:
        x_cor = int(data[data['state'] == user_answer].x)
        y_cor = int(data[data['state'] == user_answer].y)
        writer.goto(x_cor, y_cor)
        writer.write(user_answer)
        guessed_states.append(user_answer)
