import math
import numpy


def bisection(aLeft, bRight, func):
    tolerence = 0.0001
    itr = 0
    if (func(aLeft) * func(bRight) >= 0):
        print("You have not assumed right a and b\n")
        return
    middle = (aLeft+bRight)/2
    while (bRight - aLeft) / 2.0 > tolerence:
        itr += 1
        if (func(middle) == 0.0):
            print("middle is root")
            break
        if (func(aLeft)*func(middle) < 0):
            bRight = middle
        else:
            aLeft = middle
        middle = (aLeft+bRight)/2
        print("iteration: ""%d" % itr, "Left edge:", "%f" % aLeft, "right edge", "%f" % bRight, "middle:", "%f" % middle, "function value a:", "%f" % func(
            aLeft), "function value b:", "%f" % func(bRight), "function value middle:", "%f" % func(middle), "ABS:", "%f" % abs(aLeft-middle))
    print("The value of root is : ", "%f" % middle)


def bisection2(aLeft, bRight, func):
    epsilon = 0.0001
    itr = 0
    middle = aLeft+((bRight-aLeft)/2)
    while ((bRight-aLeft) > epsilon):
        itr += 1
        if (numpy.sign(func(aLeft)) != numpy.sign(func(middle))):
            bRight = middle
            bisection(aLeft, bRight, func)
        else:
            aLeft = middle
        middle = aLeft+((bRight-aLeft)/2)
        # print("iteration: ""%d" % itr, "Left edge:", "%f" % aLeft, "right edge", "%f" % bRight, "middle:", "%f" % middle, "function value a:", "%f" % func(
        #    aLeft), "function value b:", "%f" % func(bRight), "function value middle:", "%f" % func(middle), "ABS:", "%f" % abs(aLeft-middle))
    #print("The value of root is : ", "%f" % middle)
