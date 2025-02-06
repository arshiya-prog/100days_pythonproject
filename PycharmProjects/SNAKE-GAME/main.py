from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
squares = []
x = 0

for i in range(0, 3):
    tim = Turtle(shape="square")
    tim.penup()
    tim.color("white")
    tim.goto(x, 0)
    x -= 20
    squares.append(tim)

game_is_on = True
while game_is_on:
    # time.time(1)
    for sq in squares:
        sq.forward(20)
        screen.update()

screen.exitonclick()