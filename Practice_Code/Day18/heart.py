import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(1)  # Adjust the speed if needed

# Draw the heart shape
screen.bgcolor('black')
pen.width(5)
pen.color("red")
pen.begin_fill()
pen.left(140)
pen.forward(224)
pen.speed(0)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.left(120)
for _ in range(200):
    pen.right(1)
    pen.forward(2)
pen.forward(224)
pen.end_fill()

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()
