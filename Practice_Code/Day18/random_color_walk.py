import turtle
from turtle import *
import random

tim = Turtle()
tim.shape("arrow")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_color = (r, g, b)
    return my_color


# speed of turtle 0 is the fastest 10 is fast 6 is normal 3 is slow 1 is slowest:
tim.speed("fastest")
direction = [0, 90, 180, 270]
tim.pensize(15)


def random_walk():
    # tim.hideturtle()
    for i in range(500):
        tim.color(random_color())
        tim.seth(random.choice(direction))
        tim.forward(30)


random_walk()
tim.screen.mainloop()
