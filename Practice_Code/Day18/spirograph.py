import turtle
from turtle import *
import random

tim = Turtle()
tim.shape("arrow")
turtle.colormode(255)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color


def spirograph(size_of_graph):
    # tim.pensize(3)
    for i in range(int(360 / size_of_graph)):
        tim.color(random_color())
        tim.circle(100)
        tim.seth(tim.heading() + 10)


spirograph(5)
tim.circle(100)
tim.screen.mainloop()
