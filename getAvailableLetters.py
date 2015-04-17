def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    
    abet = 'abcdefghijklmnopqrstuvwxyz'
    # string.ascii_lowercase
    
    for i in range(len(lettersGuessed)):
       # print 'now on letter ',lettersGuessed[i]
        if lettersGuessed[i] in abet:
            
            abet = abet.replace(lettersGuessed[i],'')
           # print 'string is now ', abet
    
    return abet
    
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)