from random import random, randrange, randint, choice
from turtle import Turtle, Screen
import turtle

tim = Turtle()
tim.width(10)
tim.speed("fastest")
turtle.colormode(255)

directions = [0, 90, 180, 270]


def color_choice():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    cho = (r, g, b)
    return cho


for i in range(200):
    color_choice()
    tim.color(color_choice())
    tim.forward(30)
    tim.setheading(choice(directions))

screen = Screen()
screen.exitonclick()