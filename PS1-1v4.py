def countVowels(s):
    if s == '': return 0
    return int(s[0] in 'aeiouAEIOU') + countVowels(s[1:])