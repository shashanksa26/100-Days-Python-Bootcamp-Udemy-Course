from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()


def move_forward():
    tim.forward(10)


screen.onkey(key="space", fun=move_forward)

tim.screen.mainloop()
