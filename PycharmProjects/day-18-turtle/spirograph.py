from random import random, randrange, randint, choice
from turtle import Turtle, Screen
import turtle

turtle.colormode(255)

def color_choice():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    cho = (r, g, b)
    return cho

tim = Turtle()
tim.speed("fastest")

def draw_spirograph(size):
    for i in range(int(360/size)):
        tim.color(color_choice())
        tim.circle(100)
        tim.right(size)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()