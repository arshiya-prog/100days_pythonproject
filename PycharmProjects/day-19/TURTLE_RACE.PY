from turtle import Turtle, Screen
from random import choice, randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
user_bet = screen.textinput(title="Make your bet", prompt="Who do you think will win? Enter a color: ").lower()
x = -235
y = -99

for t in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[t])
    tim.penup()
    tim.goto(x, y)
    y += 33
    turtles.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in range(0, 6):
        turtles[i].forward(randint(0, 10))
        x_cor = turtles[i].xcor()
        if x_cor > 210:
            is_race_on = False
            winning_colour = turtles[i].pencolor()
            if user_bet == winning_colour:
                print(f"You won!")
            else:
                print("Your bet lost!")
            print(f"{colors[i]} won the race!")

screen.exitonclick()