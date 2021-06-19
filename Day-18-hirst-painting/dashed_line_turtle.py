from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen.exitonclick()
