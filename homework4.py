import math
import numpy
import inspect


def bisection1(aLeft, bRight, func):

    error = int(math.log((10**-(10))/(bRight-aLeft))/math.log(2))*-1
    epsilon = 0.0001
    itr = 0
    if (func(aLeft) * func(bRight) >= 0):
        return
    middle = aLeft+((bRight-aLeft)/2)
    while ((bRight-aLeft) > epsilon):
        if(itr >= error):
            return
        # print("iteration: ""%d" % itr, "Left edge:", "%f" % aLeft, "right edge", "%f" % bRight, "middle:", "%f" % middle, "function value a:", "%f" % func(
        #    aLeft), "function value b:", "%f" % func(bRight), "function value middle:", "%f" % func(middle), "ABS:", "%f" % abs(aLeft-middle))
        itr += 1
        if (func(aLeft)*func(middle) < 0):
            bRight = middle
        else:
            aLeft = middle
        middle = aLeft+((bRight-aLeft)/2)
    return middle


def derCheck(a, b, der):
    run = 0.1
    i = 0
    root = []
    while(a < b):
        if (der(a)*der(b) < 0):
            root.append(bisection1(a, b, der))
            i += i
        if(der(a) == 0.0):
            root.append(0)
            i += i
        a += run
        a = round(a, 1)
    return root


def AllRangeCheck(aLeft, bRight, func, der):
    run = 0.1
    a = aLeft
    b = bRight
    checks = []
    while(aLeft < bRight):
        if (func(aLeft)*func(aLeft+run) < 0):
            root = bisection1(aLeft, aLeft+run, func)
            print("The value of root is : ", "%f" % root)
            checks.append(aLeft+run)
        aLeft += run
        aLeft = round(aLeft, 1)
    for i in range(0, len(checks), 2):
        root_check = derCheck(float(checks[i]), float(checks[1]), der)
        for i in range(len(root_check)):
            if(func(root_check[i]) == 0):
                print("The value of root is : ", "%f" % root_check[i])


def func(x):
    return (x**4)+(x**3)-(3*(x**2))


def der(x):
    return (4*(x**3))+(3*(x**2))-6*x


a = -3
b = 2

AllRangeCheck(a, b, func, der)
