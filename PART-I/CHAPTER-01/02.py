"""
    using the combination of for loop and function in python
"""

from turtle import *
from time import sleep

shape('turtle')


def square():
    for i in range(4):
        forward(100)
        right(90)
    sleep(5)


square()
