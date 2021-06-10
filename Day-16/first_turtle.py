from turtle import Turtle, Screen

my_screen = Screen()
my_screen.bgcolor('cyan')

timmy = Turtle()
timmy.color('red')

for _ in range(3):
    timmy.forward(100)
    timmy.left(120)

my_screen.exitonclick()
