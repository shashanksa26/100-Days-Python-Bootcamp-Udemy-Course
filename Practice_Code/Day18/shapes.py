from turtle import *
import random
tim = Turtle()
tim.shape("arrow")
my_screen = Screen()


# creating a Square:
def square():
    for i in range(4):
        tim.forward(100)
        tim.left(90)


def dotted_line():
    for i in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        tim.forward(100)
        tim.left(angle)


for shape_sides in range(3, 11):
    colors = ['chartreuse', 'dark green', 'dark violet', 'green', 'SeaGreen', 'firebrick', 'gold', 'tomato', 'red',
              'blue', 'green', 'DeepSkyBlue', 'firebrick', 'wheat', 'peru']
    tim.color(random.choice(colors))
    (draw_shape(shape_sides))

# print(dotted_line())
# print(square())
my_screen.exitonclick()
