

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
            return False
    return True


# A matrix
# b matrix
# x solution

# jacob methdod


def jacobiMethod(A, b, x):
    itr = 0
    check = False
    n = len(A)
    check = isDominant(A, n)
    epsilon = 0.001
    stop = True
    if(check):
        while(stop):
            xold = x.copy()
            for i in range(n):
                sigma = 0
                for j in range(n):
                    if(i != j):
                        sigma = sigma+A[i][j]*xold[j]
                x[i] = (1/A[i][i])*(b[i]-sigma)
                print('current :', x)
            itr = itr+1
            if(abs((x[0]-xold[0])) < epsilon):
                stop = False
        print('Solution of the system is :', x, itr)
    else:
        print('matrix diagonal not dominant')

# A matrix
# b matrix
# x solution


# gauss method


def gaussMethod(A, b, x):
    itr = 0
    check = False
    n = len(A)
    epsilon = 0.001
    stop = True
    check = isDominant(A, n)
    if(check):
        while(stop):
            xold = x.copy()
            for i in range(0, n):
                sigma = b[i]
                for j in range(0, n):
                    if(j != i):
                        sigma -= A[i][j]*x[j]
                x[i] = sigma/A[i][i]
                print('current :', x)
            itr = itr+1
            if(abs((x[0]-xold[0])) < epsilon):
                stop = False
        print('Solution of the system is :', x, itr)
    else:
        print('matrix diagonal not dominant')
