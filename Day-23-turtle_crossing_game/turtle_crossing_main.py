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
screen.onkeypress(fun=player.move, key='Up')

score = Score()
cars = Car()

is_game_over = False
while not is_game_over:
    sleep(0.1)
    screen.update()
    score.display_score()
    cars.create_car()
    cars.move()
    # Detect collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            is_game_over = True
            score.display_game_over()
    # Detect turtle crossing successfully
    if player.ycor() > 280:
        score.increase_score()
        player.reset_position()
        cars.level_up()

screen.exitonclick()
