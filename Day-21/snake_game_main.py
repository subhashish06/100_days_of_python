from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

DELAY = 0.2

# Create a square screen as the game area
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# Create the snake
snake = Snake()

# Create the food
food = Food()

# Create the score board
score_board = ScoreBoard()

# Define the keystrokes to move the snake
screen.listen()
screen.onkeypress(fun=snake.left, key='Left')
screen.onkeypress(fun=snake.right, key='Right')
screen.onkeypress(fun=snake.down, key='Down')
screen.onkeypress(fun=snake.up, key='Up')

# Move the snake
is_game_over = False
while not is_game_over:
    score_board.display_score()
    screen.update()
    time.sleep(DELAY)
    snake.move()
    # Detect collision with food and move the food to new location
    if snake.head.distance(food) < 15:
        food.change_position()
        score_board.increase_score()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score_board.display_game_over()
        is_game_over = True
    # Detect collision with itself
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.display_game_over()
            is_game_over = True


screen.exitonclick()
