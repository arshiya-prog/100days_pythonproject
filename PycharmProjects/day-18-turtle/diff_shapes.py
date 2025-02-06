from random import random, randrange, randint
from turtle import Turtle, Screen
import turtle

tim = Turtle()
turtle.colormode(255)

sides = 3
degree = 120

while sides < 11:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tim.pencolor(r, g, b)
    for i in range(sides):
        tim.forward(100)
        tim.right(degree)
    sides += 1
    degree = 360 / sides

screen = Screen()
screen.exitonclick()