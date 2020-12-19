import math
import numpy
import inspect


def NewtonRaphson(func, derivFunc, x):
    epsilon = 0.0001
    itr = 0
    h = func(x) / derivFunc(x)
    while abs(h) >= epsilon:
        h = func(x)/derivFunc(x)
        x = x - h
        itr += 1
    print("The value of the root is : ", "%.4f" % x)
    print("number of iterations: ", "%d" % itr)
    return x


def SecantMethod(func, x0, x1, itr):
    step = 1
    condition = True
    epsilon = 0.0001
    while condition:
        if func(x0) == func(x1):
            print('Divide by zero error!')
            break
        x2 = x0 - (x1-x0)*func(x0)/(func(x1) - func(x0))
        x0 = x1
        x1 = x2
        step = step + 1
        if step > itr:
            break
        condition = abs(func(x2)) > epsilon
    print('Required root is: %0.8f' % x2)
    print('iterations: %d' % step)


def func(x):
    return (x**4)+(x**3)-(3*(x**2))


def der(x):
    return (4*(x**3))+(3*(x**2))-6*x


NewtonRaphson(func, der, -20)
SecantMethod(func, -3, 2, 20)
