import math

def derivative(f, x, h):
    ans = (1.0/(2*h))*(f(x+h)-f(x-h)) 
    return ans 

def solve(f, x0, h): 
    while True:
        var = x0 - (f(x0)) / derivative(f, x0, h) #Kör x0 - funktionen genom dess derivata och sparar detta i en ny variabel (var)
        if abs(var - x0) < h: #Kollar om beloppet av var minus den ursprungliga x0 är mindre än det tillåtna felet h, om detta är fallet har vi kommit fram till ett nollställe
            return var #Ifall detta är fallet bryts loopen och funktionen returnerar nollstället (var)
        x0 = var #Om var - x0 fortfarande är för stort så erstätts x0 med var. Detta så att funktionen kan prövas igen fast med ett uppdaterat x0. Detta kommer till slut ta oss till ett nollställe

def func1(x):
    return x**2 - 1

def func2(x):
    return x - math.e**(-x) 

print(solve(math.sin, 4, 0.001))
print(solve(func1, -4, 0.0001))
print(solve(func2, 3, 0.0001))
