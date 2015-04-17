def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTup = ()
    for i in range(0,len(aTup)):
       if i==0 or i%2==0:
           newTup = newTup + (aTup[i],)
       #print 'i is ', i
       #print 'aTup(i) is ', aTup[i]
    
    return newTup