def findDivisors(d1,d2):
    divs = ()
    for i in range(1, min(d1,d2) + 1):
        if d1%i == 0 and d2%i == 0:
            divs += (i,)
    return divs