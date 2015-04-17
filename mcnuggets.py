def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.

    """
    
    
    s = 6
    m = 9
    l = 20
    g1 = n % l
    g2 = g1 % m
    g3 = g2 % s
    g4 = g1 % s
    g5 = n % m
    g6 = g5 % s
    g7 = n % s
    
    results = [g1,g2,g3,g4,g5,g6,g7]
    
    for i in results:
        if i == 0:
            return True
            
    return False
        
    # try all combinations
    
    
        
    
        