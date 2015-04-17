def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.

    """
    
    
    s = 0
    m = 0
    l = 0
   

        

    for i in range(int(n/6)+1):
        if 6*(s+i+1)+9*m+20*l == n:
            return True
        for j in range(int(n/9)+1):
            if 6*(s+i)+9*(m+j+1)+20*l == n:
                return True
            for k in range(int(n/20)+1):
                if 6*(s+i)+9*(m+j)+20*(k+l+1) == n:
                    return True

    return False     

        
    # try all combinations
    
    
        
    
        