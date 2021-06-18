from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor=0, y_cor=0):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(x=x_cor, y=y_cor)

    def move_up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
