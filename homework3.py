import math
from numpy import linalg as LA

# A matrix
# b matrix
# x solution
# n size

# jacob methdo


def jacobiMethod(A, b, x, n):
    itr = 0
    tol = 1e-5
    normVal = math.inf
    while(normVal > tol):
        xold = x
        for i in range(n):
            sigma = 0
            for j in range(n):
                if(i != j):
                    sigma = sigma+A[i, j]*x[j]
            x[i] = (1/A[i, i])*(b[i]-sigma)
        itr = itr+1
        normVal = abs(xold-x)
    print('Solution of the system is : \n%f\n%f\n%f\n%f in %d iterations', x, itr)

# A matrix
# b matrix
# x solution
# n size

# gauss method


def gaussMethod(A, b, x, n):
    itr = 0
    tol = 1e-5
    normVal = math.inf
    while(normVal > tol):
        x_old = x
        for i in range(n):
            sigma = 0
            for j in range(i-1):
                sigma = sigma+A[i, j]*x[j]
            for j in range(i+1, n):
                sigma = sigma+A[i, j]*x_old[j]
            x[i] = (1/A[i, i])*(b[i]-sigma)
        itr = itr+1
        normVal = LA.norm(x_old, x)
    print('Solution of the system is : \n%f\n%f\n%f\n%f in %d iterations', x, itr)


# m=matrix
# n=number of rows and columns

# if matrix diagonal is dominant
def isDominant(m, n):
    for i in range(0, n):
        sum = 0
        for j in range(0, n):
            sum = sum + abs(m[i][j])
        sum = sum - abs(m[i][i])
        if (abs(m[i][i]) < sum):
            print("is not dominant")
    print("is dominant")
