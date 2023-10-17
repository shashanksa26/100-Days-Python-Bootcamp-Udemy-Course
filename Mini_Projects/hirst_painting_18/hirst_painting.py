import turtle
from turtle import *
import colorgram
import random


# extract color from image
tim = Turtle()


def extract_colors():
    colors = colorgram.extract('image.jpg', 30)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    print(rgb_colors)
# extract_colors()


turtle.colormode(255)
color_list = [(149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

# properties of the pen
tim.speed(0)
tim.hideturtle()
tim.penup()
tim.seth(225)  # setting the direction of the turtle by degree
tim.forward(300)
tim.seth(0)
number_of_dots = 100

# loop to print the dot
for dots_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dots_count % 10 == 0:
        tim.seth(90)
        tim.forward(50)
        tim.seth(180)
        tim.forward(500)
        tim.seth(0)


# to keep the screen on until we terminate
tim.screen.mainloop()


