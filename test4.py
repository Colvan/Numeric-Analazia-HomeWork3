from homework4 import *


def func(x):
    return x*x - 4*math.sin(x)


def func2(x):
    return (x*x*x*x)-(x*x*x)-(3*x*x)


def func3(x):
    return(x*x*x)-x-1


a = -3
b = 2
# big range
bisection2(a, b, func2)

# small range
# bisection2(a, b, func2)
