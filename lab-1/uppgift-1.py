def kostnad(P, r, a):
    k = P +(a+1)*P*r/2
    print(f"Den totala kostnaden efter {a} år är {k:.0f} kronor.")

kostnad(50000, 0.03, 10)