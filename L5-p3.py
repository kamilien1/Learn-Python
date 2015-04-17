def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here

    if exp == 0:
        return 1
    elif (exp % 2) == 0:
        #print 'even, exp is ', exp
        return recurPowerNew(base*base, exp/2)
    else:
        #print 'odd, exp is '
        return base * recurPowerNew(base, exp-1)