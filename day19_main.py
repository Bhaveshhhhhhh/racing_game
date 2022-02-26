# 1) sketch maker using turtle module

# from turtle import Turtle, Screen
#
# tim = Turtle()
# tim.shape("turtle")
# tim.pensize(3)
# screen = Screen()
#
# def move_forwd():
#     tim.forward(10)
#
# def move_right():
#     tim.right(10)
#
# def move_left():
#     tim.left(10)
#
# def move_back():
#     tim.backward(10)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwd)
# screen.onkey(key="a", fun=move_right)
# screen.onkey(key="d", fun=move_left)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="x", fun=clear)
# screen.exitonclick()

# 2) turtle racing game
import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter the colour")

colours = ["red", "orange", "yellow", "purple", "blue", "green"]
y_postion = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    tim = Turtle()
    tim.color(colours[turtle_index])
    tim.shape("turtle")
    tim.penup()
    tim.goto(x=-230, y=y_postion[turtle_index])
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print(f"You Are Winner {winning_colour} turtle wins!!")
            else:
                print(f"you lose!!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()