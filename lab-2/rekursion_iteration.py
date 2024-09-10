def bounce(n):
    if n == 0:
        print(0)
    else:
        print(n)
        bounce(n-1)
        print(n)

def bounce2(n):
    for i in range(n, 0, -1):
        print(i)

    for i in range(0, n+1):
        print(i)

def tvarsumman(tal):
    if tal < 10:
        return tal
    
    else:
        return tal % 10 + tvarsumman(tal // 10)

def tvarsumman2(tal):
    resultat = 0

    while tal > 0:
        resultat += tal % 10
        tal = tal // 10
    return resultat

