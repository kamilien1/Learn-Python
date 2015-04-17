def myLog(x, b):

    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    root = 0
    if x < b:
        print 'X must be greater than b'        
    else:
        while b**root < x:
            if b**(root+1) <= x:
                root += 1
    
    

        print 'Log base',b,'of',x,'is',root
