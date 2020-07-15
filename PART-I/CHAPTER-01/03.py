"""
    using variables
"""

from turtle import *
from time import sleep

shape('turtle')


def square(sidelength):
    for i in range(4):
        forward(sidelength)
        right(90)
    sleep(5)


square(30)
square(50)
square(100)
