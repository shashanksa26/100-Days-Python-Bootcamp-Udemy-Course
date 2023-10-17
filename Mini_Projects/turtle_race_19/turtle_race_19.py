from turtle import Turtle, Screen
import random

screen = Screen()
screen.listen()
screen.setup(width=500, height=400)
user_bet = (screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: \n"
                                                          "Red, Orange, Yellow, Green, Blue, Purple")).lower()
print(user_bet)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_pos = [-70, -40, -10, 20, 50, 80]

is_race_on = False
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet in colors:
    is_race_on = True
else:
    print("The chosen Color of the Turtle is not valid")
    screen.bye()
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            # here 230 is given because 250- 40/2 =230 here 40/2 is the area covered by the turtle
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner! Better luck next time!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.mainloop()
