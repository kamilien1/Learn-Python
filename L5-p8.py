def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here

    if len(aStr) == 0:
        return False
        
    elif char == aStr[len(aStr)/2]:
        return True
    
    elif len(aStr) == 1:
        return False
        
    elif char > aStr[len(aStr)/2]:
        return isIn(char,aStr[len(aStr)/2:])
    
    elif char < aStr[len(aStr)/2]:
        return isIn(char,aStr[:len(aStr)/2])
        
    else:
        return False