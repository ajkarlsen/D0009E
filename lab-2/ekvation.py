import math

def derivative(f, x, h):
    ans = (1.0/(2*h))*(f(x+h)-f(x-h))
    return ans 

#derivative(math.sin, math.pi, 0.0001)
#derivative(math.cos, math.pi, 0.0001)
#derivative(math.sin, math.pi/2, 0.0001)



def solve(f, x0, h):
    while True:
        var = x0 - (f(x0)) / derivative(f, x0, h)
        if abs(var - x0) < h:
            return var
        x0 = var

print(solve(math.sin, math.pi, 0.0001))