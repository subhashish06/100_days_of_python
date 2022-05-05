"""
Program: Turtle Crossing Car Game
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Screen
from time import sleep
from car import Car
from player import Player
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
screen.onkeypress(fun=player.move, key="Up")

score = Score()
cars = Car()

GAME_OVER = False
while not GAME_OVER:
    sleep(0.1)
    screen.update()
    score.display_score()
    cars.create_car()
    cars.move()
    # Detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            GAME_OVER = True
            score.display_game_over()
    # Detect turtle crossing successfully
    if player.ycor() > 280:
        score.increase_score()
        player.reset_position()
        cars.level_up()

screen.exitonclick()
