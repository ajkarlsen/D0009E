import math

def derivative(f, x, h):
    ans = 1.0/(2*h)*(f(x+h)-f(x-h))
    return ans

print(derivative(math.sin, math.pi, 0.0001))
