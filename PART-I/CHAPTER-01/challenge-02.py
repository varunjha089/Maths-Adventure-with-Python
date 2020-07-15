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


def multi_square():
    for i in range(60):
        right(5)
        square()
    sleep(10)


multi_square()
