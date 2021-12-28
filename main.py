import turtle
from turtle import Turtle, Screen
import random

goldy = Turtle()
goldy.speed(50)
turtle.colormode(255)


def rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for _ in range(int(360/10)):
    side = 0
    goldy.color(rgb())
    goldy.circle(100)
    side -= 10
    goldy.right(side)

screen = Screen()
screen.exitonclick()
