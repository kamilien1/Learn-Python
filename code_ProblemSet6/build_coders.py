import string

def buildCoders(n):
    
    # shift by n to the right
    # return key value pair 
    
    lp = string.ascii_lowercase
    up = string.ascii_uppercase
    sl = {}
    su = {}
    
    for i in range(0,26):
        sl[lp[i]]=lp[(i+n)%26]
        su[up[i]]=up[(i+n)%26]
    
    cs = dict(sl.items()+su.items())
    return cs
    

def applyCoders(astr,coder):
    
    ns = ''
    for i in astr:
        if i in coder:
            ns+=coder[i]
        else:
            ns+=i
    
    return ns
    
def applyShift(text, shift):
    
    
    ss = buildCoders(shift)
    return applyCoders(text, ss)


word_list = open('words.txt',r)

def findBestShift(wordlist, text):
    
    # break texts into words
    # remove commas and other chars
    
    # list of text words
    # decipher 
    
a = buildCoders(5)
b =applyCoders('Hello, dear!',a)
print b

c = applyShift('Whats up world?',5)
print c
