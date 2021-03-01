#Brandon Escamilla PSID:1823960
# Numerous engineering and scientific applications require finding solutions to a set of equations. Ex: 8x + 7y = 38 and 3x - 5y = -1 have a solution x = 3, y = 2.
# Given integer coefficients of two linear equations with variables x and y, use brute force to find an integer solution for x and y in the range -10 to 10.
#
# Ex: If the input is:
#
# 8
# 7
# 38
# 3
# -5
# -1
# Then the output is:
#
# 3 2

#a(x) + b(y) = c   this is setting up the equations for our linear equations.
a = int(input())
b = int(input())
c = int(input())

#d(x) + e(y) = f   this is setting up the equations for our linear equations.
d = int(input())
e = int(input())
f = int(input())


#were setting up functions so that we dont have to code the work. THIS IS BRUTE FORCE
def func1(x, y):
    return a * x + b * y - c

#were setting up functions so that we dont have to code the work. THIS IS BRUTE FORCE
def func2(x, y):
    return d * x + e * y - f


finalx = 100
finaly = 100
for x in range(-10, 11):
    for y in range(-10, 11):
        if func1(x, y) == func2(x, y) and func1(x, y) == 0:
            finalx = x
            finaly = y
if finalx != 100:
    print(finalx, finaly)
else:
    print('No solution')