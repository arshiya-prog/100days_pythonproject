from random import choice
from turtle import Turtle, Screen
import turtle
import colorgram

turtle.colormode(255)
tim = Turtle()
rgb_colors = []
tim.speed("fastest")

# colors = colorgram.extract("spot_painting.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tup = (r, g, b)
#     rgb_colors.append(tup)

color_list = [(219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (118, 82, 93), (179, 140, 150), (41, 46, 65), (162, 104, 151), (126, 173, 114), (83, 96, 183), (67, 9, 27), (81, 133, 107), (231, 188, 138), (52, 62, 79), (195, 90, 72), (116, 43, 58), (60, 41, 28), (92, 144, 117), (70, 67, 52), (182, 187, 207), (211, 181, 189), (102, 51, 38), (174, 199, 203), (181, 201, 180), (210, 184, 180), (41, 73, 82)]

tim.hideturtle()
tim.setheading(225)
tim.penup()
tim.forward(250)
tim.setheading(0)
tim.pendown()

x = tim.xcor()
y = tim.ycor()

for j in range(10):
    for i in range(10):
        tim.dot(20, choice(color_list))
        tim.penup()
        tim.forward(50)
    tim.setpos(x, y+50)
    y += 50

screen = Screen()
screen.exitonclick()