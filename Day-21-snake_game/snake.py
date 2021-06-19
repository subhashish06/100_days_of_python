from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def extend(self):
        self.add_segment(self.snake_segments[-1].pos())

    def add_segment(self, position):
        snake = Turtle(shape='square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.snake_segments.append(snake)

    def move(self):
        for segment_index in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_index - 1].xcor()
            new_y = self.snake_segments[segment_index - 1].ycor()
            self.snake_segments[segment_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
