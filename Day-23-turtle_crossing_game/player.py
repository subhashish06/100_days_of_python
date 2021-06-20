from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISHING_POSITION_Y = 280
PACE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.reset_position()
        self.setheading(90)

    def move(self):
        self.forward(PACE)

    def reset_position(self):
        self.goto(STARTING_POSITION)
