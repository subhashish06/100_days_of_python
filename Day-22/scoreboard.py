from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 20, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()

    def display_score(self):
        self.clear()
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def display_game_over(self):
        self.home()
        self.write(f'GAME OVER', align=ALIGNMENT, font=FONT)


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.pensize(10)
        self.hideturtle()
        self.goto(x=0, y=-300)
        self.setheading(90)
        while self.ycor() < 300:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
