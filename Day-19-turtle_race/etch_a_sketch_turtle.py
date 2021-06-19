from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.forward(-10)


def move_clockwise():
    tim.right(5)


def move_counter_clockwise():
    tim.left(5)


def clear_drawing():
    tim.clear()
    tim.reset()


screen.listen()
screen.onkeypress(fun=move_forward, key='Up')
screen.onkeypress(fun=move_backward, key='Down')
screen.onkeypress(fun=move_clockwise, key='Right')
screen.onkeypress(fun=move_counter_clockwise, key='Left')
screen.onkey(fun=clear_drawing, key='c')

screen.exitonclick()
