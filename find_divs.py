def findMaxdivs(d1,d2):
#    divs = ()
    Min, Max = None, None
    
    for i in range(2,min(d1,d2)+1):
        if d1%i == 0 and d2%i == 0:
            if Min == None or i < Min:
                Min = i
            if Max == None or i > Max:
                Max = i
    return (Min, Max)