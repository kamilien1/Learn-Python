# s = 'azcbobobegghakl'
s = 'abcdefg'

temp = s[0]
longestString = temp
i = 0

while i < len(s)-1:
    if s[i] <= s[i+1]:
        temp +=s[i+1]
    elif len(longestString) < len(temp):
        longestString = temp
        temp = s[i+1]
    i+=1

print('Longest substring in alphabetical order is: ' + longestString)

