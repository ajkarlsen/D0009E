import math

def derivative(f, x, h):
    ans = (1.0/(2*h))*(f(x+h)-f(x-h)) 
    return ans 

def solve(f, x0, h):
    while True:
        var = x0 - (f(x0)) / derivative(f, x0, h)
        if abs(var - x0) < h:
            return var
        x0 = var

def func1(x):
    return x**2 - 1

def func2(x):
    return x - math.e**(-x) 

print(solve(math.sin, 4, 0.001))
print(solve(func1, -4, 0.0001))
print(solve(func2, 3, 0.0001))
