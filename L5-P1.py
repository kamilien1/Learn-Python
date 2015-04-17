def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    temp = base 
    # Your code here
    if exp == 0:
        return 1
    else:
        while exp > 1:
            temp = temp * base
            exp -= 1
         #   print 'base is ', temp
        return temp
                                                