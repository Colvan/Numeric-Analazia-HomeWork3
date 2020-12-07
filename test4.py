from homework4 import *


def func(x):
    return (x**4)+(x**3)-(3*(x**2))


def der(x):
    return (4*(x**3))+(3*(x**2))-6*x


a = -3
b = 2

AllRangeCheck(a, b, func, der)
