# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/Kamil/GDrive/Clients and Projects/Learn Python/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    if len(lettersGuessed) == 0:
        return False
    
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            if i == (len(secretWord)-1):
                return True 
        else:
            return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...


    aStr = ''
    
    if len(lettersGuessed) == 0:
        
        return ' _ ' * len(secretWord)
    
    for i in range(len(secretWord)):
        
        if secretWord[i] in lettersGuessed:
            
            aStr += secretWord[i]
        
        else:
        
            aStr += ' _ '
        
    return aStr

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...

    abet = 'abcdefghijklmnopqrstuvwxyz'
    # string.ascii_lowercase
    if lettersGuessed == []:
        return abet
        
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in abet:
            abet = abet.replace(lettersGuessed[i],'')
    
    return abet    
            

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...

    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is', len(secretWord), 'letters long'

    lettersGuessed = []
    availableLetters = 'abcdefghijklmnopqrstuvwxyz'
    guessesLeft = 8
    
    while guessesLeft > 0:
        
        print '-----------'
        print 'You have',guessesLeft, 'guesses left'
        print 'Available letters: ', availableLetters
        lettersGuessed += raw_input('Please guess a letter: ').lower()
        
        # if letter has not been guessed before and letter is in secret word
        if lettersGuessed[-1] in secretWord and lettersGuessed[-1] not in lettersGuessed[0:-1]:
            print 'Good guess: ', getGuessedWord(secretWord, lettersGuessed)
            availableLetters = getAvailableLetters(lettersGuessed)

        # already guessed that letter 
        elif lettersGuessed[-1] in lettersGuessed[0:-1]:
            print 'Oops! You\'ve already guessed that letter: ', getGuessedWord(secretWord, lettersGuessed)

        # did not guess a letter, -1 guesses left
        else: 
            print 'Oops! That letter is not in my word: ', getGuessedWord(secretWord, lettersGuessed)
            availableLetters = getAvailableLetters(lettersGuessed)
            guessesLeft -= 1
        
        if isWordGuessed(secretWord, lettersGuessed):
            print '-----------'
            print 'Congratulations, you won!'
            return
    
    if guessesLeft == 0 and isWordGuessed(secretWord, lettersGuessed) == False:
        print '-----------'
        print 'Sorry, you ran out of guesses. The word was ', secretWord
        return
        

    
    # loop through guesses
        # available letters are 
        # please guess a letter
            # if letter is in word
                # print 'Good guess ' printout guesses
                # update guessed letter list
            # elif letter already guessed
                # print oops you already guessed this letter!
            # else
                # print you failed! 
                # bad guesses += 1
            
        # if badguesses == 8
            # end game, bad job
            # print secretWord
            
        # if word found
            # end game, good job
            # Congrats, you won


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()

secretWord = 'y'
hangman(secretWord)
