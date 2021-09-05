"""
Program: Ping Pong Ball Module
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle


class Ball(Turtle):
    """creates the ball object"""
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.setheading(220)
        self.is_moving = True
        self.ball_speed = 0.1

    def move(self):
        """moves the ball on the screen"""
        if 0 < self.heading() < 90:
            new_x = self.xcor() + 10
            new_y = self.ycor() + 10
            self.goto(x=new_x, y=new_y)
        elif 90 < self.heading() < 180:
            new_x = self.xcor() - 10
            new_y = self.ycor() + 10
            self.goto(x=new_x, y=new_y)
        elif 180 < self.heading() < 270:
            new_x = self.xcor() - 10
            new_y = self.ycor() - 10
            self.goto(x=new_x, y=new_y)
        else:
            new_x = self.xcor() + 10
            new_y = self.ycor() - 10
            self.goto(x=new_x, y=new_y)

    def bounce_off_wall(self):
        """bounces the ball off the wall"""
        new_heading = 360 - self.heading()
        self.setheading(new_heading)

    def bounce_off_paddle(self):
        """bounces the ball off the paddle"""
        new_heading = 180 - self.heading()
        if new_heading < 0:
            new_heading += 360
        self.setheading(new_heading)

    def speed_up(self):
        """speeds up the ball"""
        self.ball_speed *= 0.9
