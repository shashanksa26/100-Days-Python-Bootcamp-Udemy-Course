from turtle import *
import random

tim = Turtle()
tim.shape("arrow")

colors = ['chartreuse', 'dark green', 'dark violet', 'green', 'SeaGreen', 'firebrick', 'gold', 'tomato', 'red',
          'blue', 'green', 'DeepSkyBlue', 'firebrick', 'wheat', 'peru']

# speed of turtle 0 is the fastest 10 is fast 6 is normal 3 is slow 1 is slowest:
tim.speed("fastest")
direction = [0, 90, 180, 270]
tim.pensize(25)


def random_walk():
    # tim.hideturtle()
    for i in range(500):
        tim.color(random.choice(colors))
        tim.seth(random.choice(direction))
        tim.forward(30)


random_walk()
tim.screen.mainloop()
