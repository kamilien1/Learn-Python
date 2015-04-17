def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if len(lettersGuessed) == 0:
#        print 'length is ', len(lettersGuessed)
        return False
            
    for i in range(len(secretWord)):
 #       print 'at i = ',i
        if secretWord[i] in lettersGuessed:
  #          print i, ' found letter ', secretWord[i]
            if i == (len(secretWord)-1):
   #             print 'Found word ', secretWord
                return True 
        else:
          #  print 'ended on letter ', secretWord[i]
            return False
 
# testing stuff
               
#secretWord = 'apple'
#lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#print isWordGuessed(secretWord, lettersGuessed)

#print isWordGuessed('broccoli', [])