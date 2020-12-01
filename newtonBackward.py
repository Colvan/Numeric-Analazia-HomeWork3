# x number of given value
# y is used for difference table
# with y[][0] used for input
# vlaue to interpolate at

def newtonBackward(x, y, value):

    # len of x
    n = len(x)
# calculating factorial of given number n

    def fact(n):
        f = 1
        for i in range(2, n + 1):
            f *= i
        return f
# calculating u mentioned in the formula

    def u_cal(u, n):
        temp = u
        for i in range(1, n):
            temp = temp * (u + i)
        return temp
# Calculating the forward difference
# table
    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            y[j][i] = y[j][i-1] - y[j-1][i-1]
# Displaying the forward difference table
    print("BACKWARD DIFFERENCE TABLE")
    for i in range(n):
        print(x[i], end="\t")
        for j in range(i+1):
            print(y[i][j], end="\t")
        print("")

# initializing u and sum
    sum = y[n - 1][0]
    u = (value - x[n - 1]) / (x[1] - x[0])
    for i in range(1, n):
        sum = sum + (u_cal(u, i) * y[n-1][i]) / fact(i)
    print("\nValue at", value, "is", round(sum, 6))


n = 5
x = [20, 30, 40, 50, 60]
y = [[0 for i in range(n)]
     for j in range(n)]
y[0][0] = 33
y[1][0] = 71
y[2][0] = 118
y[3][0] = 163
y[4][0] = 188
value = 65
#newtonBackward(x, y, value)


x = [1891, 1901, 1911, 1921, 1931]
y = [[0 for i in range(n)]
     for j in range(n)]
y[0][0] = 46
y[1][0] = 66
y[2][0] = 81
y[3][0] = 93
y[4][0] = 101
value = 1925

newtonBackward(x, y, value)
