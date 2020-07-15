"""
    Will be creating a spirograph using python's Turtle module
"""

from turtle import *
from time import sleep

bgcolor('black')
pensize(2)
speed(0)

colors = ['red', 'orange', 'blue', 'purple', 'green', 'yellow', 'white']

for i in range(6):
    for colours in colors:
        color(colours)
        circle(100)
        left(10)
hideturtle()
sleep(20)