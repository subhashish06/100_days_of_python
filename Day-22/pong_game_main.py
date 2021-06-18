from turtle import Screen
from time import sleep
from paddle import Paddle
from ball import Ball
from scoreboard import Score, Net

DELAY = 0.1

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Classic Pong')
screen.tracer(0)

right_paddle = Paddle(x_cor=350, y_cor=0)
left_paddle = Paddle(x_cor=-350, y_cor=0)
ball = Ball()
left_score = Score()
left_score.goto(-100, 250)
right_score = Score()
right_score.goto(100, 250)
net = Net()

screen.listen()
screen.onkeypress(fun=right_paddle.move_up, key='Up')
screen.onkeypress(fun=right_paddle.move_down, key='Down')
screen.onkeypress(fun=left_paddle.move_up, key='w')
screen.onkeypress(fun=left_paddle.move_down, key='s')

is_game_over = False
while not is_game_over:
    sleep(DELAY)
    screen.update()
    ball.move()
    left_score.display_score()
    right_score.display_score()
    # Detect ball bouncing off wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_off_wall()
    # Detect ball hitting the paddle.
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) \
            or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_off_paddle()
    # Detect ball missing the right paddle.
    if ball.xcor() > 400:
        left_score.increase_score()
        ball.goto(0, 0)
        ball.bounce_off_paddle()
    # Detect ball missing the left paddle.
    if ball.xcor() < -400:
        right_score.increase_score()
        ball.goto(0, 0)
        ball.bounce_off_paddle()
    if right_score.score > 14 or left_score.score > 14:
        is_game_over = True
        left_score.display_score()
        right_score.display_score()
        right_score.display_game_over()

screen.exitonclick()
