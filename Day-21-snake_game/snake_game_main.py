"""
Program: Snake Game
Author: Subhashish Dhar
Date: 03/09/2021
"""

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard, HighScore

DELAY = 0.8

# Create a square screen as the game area
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game [Press 'R' key to reset the high score]")
screen.tracer(0)

# Create the snake
snake = Snake()

# Create the food
food = Food()

# Create the score board
score_board = ScoreBoard()
high_score = HighScore()

# Define the keystrokes to move the snake
screen.listen()
screen.onkeypress(fun=snake.left, key="Left")
screen.onkeypress(fun=snake.right, key="Right")
screen.onkeypress(fun=snake.turn_down, key="Down")
screen.onkeypress(fun=snake.turn_up, key="Up")
screen.onkeypress(fun=high_score.reset_high_score, key="r")

# Move the snake
GAME_OVER = False
while not GAME_OVER:
    score_board.display_score()
    time.sleep(DELAY)
    snake.move()
    screen.update()
    # Detect collision with food and move the food to new location
    if snake.head.distance(food) < 15:
        food.change_position()
        score_board.increase_score()
        snake.extend()
    # Detect collision with wall
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        score_board.display_game_over()
        GAME_OVER = True
        high_score.update_high_score(score=score_board.score)
    # Detect collision with itself
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.display_game_over()
            GAME_OVER = True
            high_score.update_high_score(score=score_board.score)

screen.exitonclick()
