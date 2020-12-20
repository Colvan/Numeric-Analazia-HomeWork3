import math
import numpy
import inspect


def NewtonRaphson(func, derivFunc, x):
    epsilon = 0.0001
    itr = 0
    while True:
        if(derivFunc(x) == 0):
            break
        itr += 1
        x1 = x - (func(x)/derivFunc(x))
        t = abs(x1-x)
        x = x1
        if(t < epsilon):
            break
    print('Required root is: %0.3f' % x)
    print('iterations: %d' % itr)


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
    print('Required root is: %0.3f' % x2)
    print('iterations: %d' % step)


def func(x):
    return (x**4)+(x**3)-(3*(x**2))


def der(x):
    return (4*(x**3))+(3*(x**2))-6*x


# NewtonRaphson(func, der, 10)
# SecantMethod(func, -3, 2, 100)


def run(left, right, func, der):
    arr1 = []
    arr2 = []
    for i in range(left, right):
        if (func(i) * func(i + 1)) < 0 or (func(i) * func(i + 1)) == 0:
            arr1.append((i, i + 1))
            arr2.append((i, i + 1))
    print("----------------NEWTON RAPHSON METHOD-----------------------")
    for i in arr1:
        NewtonRaphson(func, der, i[0])
    print("-------------------------Secant METHOD----------------------")
    for i in arr2:
        SecantMethod(func, i[0], i[1], 100)


run(-3, 2, func, der)
