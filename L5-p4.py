def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    c = min(abs(a),abs(b))
    
    while c > 0:
        if a%c == 0 and b%c == 0:
            return c
        else:
            c-=1
                     
    return c