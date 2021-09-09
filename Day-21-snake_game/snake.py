"""
Program: Snake Module
Author: Subhashish Dhar
Date: 03/09/2021
"""

from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    """The Snake Class"""
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        """creates the snake segments"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        """elongates the snake"""
        self.add_segment(self.snake_segments[-1].pos())

    def add_segment(self, position):
        """adds segments to the snake"""
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snake_segments.append(snake)

    def move(self):
        """moves the snake"""
        for segment_index in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_index - 1].xcor()
            new_y = self.snake_segments[segment_index - 1].ycor()
            self.snake_segments[segment_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        """turns the snake right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """turns the snake left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_up(self):
        """turns the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        """turns the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
