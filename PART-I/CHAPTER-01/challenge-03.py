"""
    This is challenge 03
    In this module I am solving challenge 03
"""

from turtle import *
from time import sleep

shape('turtle')


def triangle(side_length):
    for i in range(3):
        forward(side_length)
        right(120)
    sleep(5)


triangle(200)
