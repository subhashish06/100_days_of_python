from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=800, height=400)
is_game_on = False
user_bet = screen.textinput(title='Enter your bet',
                            prompt='Which turtle will win the race? red/green/blue/gray/pink/purple : ')
colors = ['red', 'green', 'blue', 'gray', 'pink', 'purple']
all_turtles = []

y = -150
for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(-390, y)
    y += 60
    all_turtles.append(new_turtle)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 370:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! {winning_color} has won the race.")
            else:
                print(f"You lost! {winning_color} has won the race.")
            is_game_on = False
        else:
            rand_distance = randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
