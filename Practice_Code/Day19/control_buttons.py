from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def clear_screen():
    tim.reset()


def counter_clockwise():
    tim.left(10)
    tim.heading()


def clockwise():
    tim.right(10)
    tim.heading()


screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key="c", fun=clear_screen)



tim.screen.mainloop()
