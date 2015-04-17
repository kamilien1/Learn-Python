def isPalindrome(s):
    
    
    def toChars(s):
        s = s.lower()
        ans = ''
        
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyk':
                ans += c
        return ans
        
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            ans = s[0] == s[-1] and isPal(s[1:-1])
            return ans
    
    return isPal(toChars(s))
    
def testIsPal():
    print 'trying dogGod'
    print isPalindrome('dogGod')
    print 'trying dogood'
    print isPalindrome('dogood')