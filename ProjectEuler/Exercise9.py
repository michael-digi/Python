for a in range(1, 500):
    for b in range(a, 500):
        c = 1000 - a - b
        if c**2 == a**2 + b**2:
                print (a*b*c)
                print(a,b,c)
                break