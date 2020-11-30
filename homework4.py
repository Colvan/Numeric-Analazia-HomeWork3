import math
import numpy


def bisection(aLeft, bRight, func):
    epsilon = 0.0001
    if (func(aLeft) * func(bRight) >= 0):
        print("You have not assumed right a and b\n")
        return
    while ((bRight-aLeft) >= epsilon):
        middle = (aLeft+bRight)/2
        if (func(middle) == 0.0):
            print("middle is root")
            break
        if (func(aLeft)*func(middle) < 0):
            bRight = middle
        else:
            aLeft = middle
        print("The value of root is : ", "%f" % aLeft, "%f" %
              func(aLeft), "%f" % bRight, "%f" % func(bRight), "%f" % middle)
    print("The value of root is : ", "%f" % aLeft, "%f" %
          func(aLeft), "%f" % bRight, "%f" % func(bRight), "%f" % middle)


def bisection2(aLeft, bRight, func):
    epsilon = 0.001
    while ((bRight-aLeft) > epsilon):
        middle = aLeft+((bRight-aLeft)/2)
        if (numpy.sign(func(aLeft)) == numpy.sign(func(middle))):
            aLeft = middle
        else:
            bRight = middle
        print("The value of root is : ", "%f" % aLeft, "%f" %
              func(aLeft), "%f" % bRight, "%f" % func(bRight), "%f" % middle)
    print("The value of root is : ", "%f" % aLeft, "%f" %
          func(aLeft), "%f" % bRight, "%f" % func(bRight), "%f" % middle)
