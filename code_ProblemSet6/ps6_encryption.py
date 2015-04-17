# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "../words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShift(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """

    # shift by n to the right
    # return key value pair 
    
    lp = string.ascii_lowercase
    up = string.ascii_uppercase
    sl = {}
    su = {}
    
    for i in range(0,26):
        sl[lp[i]]=lp[(i+shift)%26]
        su[up[i]]=up[(i+shift)%26]
    
    cs = dict(sl.items()+su.items())
    return cs
    
    

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ns = ''
    for i in text:
        if i in coder:
            ns+=coder[i]
        else:
            ns+=i
    
    return ns
    
def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ss = buildCoder(shift)
    return applyCoder(text, ss)    

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    
    # loadWords() isWord(wordList, word)
    # break down text
    # maxW=len(stripped-text)
    # maxTrue = 0
    # temp true = 0
    # for 0 to 26
    # isword true on text[0:maxW]
    # temp++
    # if maxTrue == maxW
    # return counter

    # use isword on text[0:maxW]
    # for 0 to maxW, 
    # note: find function (given to us, however, should use binary search)
    


    most_true = 0
    best_range = 0
    for i in range(0,26):
        # shift text 
        sw_shift = applyShift(text,i)
        sw_shift = sw_shift.split(' ')
#        print sw_shift
        temp_true = 0
        for j in range(0,len(sw_shift)):
            temp_true+=isWord(wordList,sw_shift[j])
        
 #       print 'for i=',i,'temp_true=',temp_true
        
        if temp_true > most_true:
            most_true = temp_true
            best_range = i
            
        if most_true == len(sw_shift):
            print applyShift(text,i)
            return i
#    print 'not most true, except...'+applyShift(text,best_range)
    return best_range

    
def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
   
    story = getStoryString()    
    wordList = loadWords()
    best_shift = findBestShift(wordList, story)
    story_decrypted = applyShift(story, best_shift)
    return story_decrypted
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    '''
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    
    assert applyShift(s, bestShift) == 'Hello, world!'
    '''
    # To test decryptStory, comment the above four lines and uncomment this line:
    print decryptStory()
    