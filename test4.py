from homework4 import *


def func(x):
    return x*x - 4*math.sin(x)


a = 1
b = 3
#bisection(a, b, func)
bisection2(a, b, func)
