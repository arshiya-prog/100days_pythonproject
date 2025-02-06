from random import random, randrange, randint, choice
from turtle import Turtle, Screen
import turtle
import colorgram

turtle.colormode(255)
tim = Turtle()

def color_choice():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    cho = (r, g, b)
    return cho



screen = Screen()
screen.exitonclick()