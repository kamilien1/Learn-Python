# s = 'azcbobobegghakl'
# s = 'abc'
#s = 'abcbcd'
s = 'axdjemzyljfjowtppdxhizji'

marker = s[0]
longestString = marker

for i in range(0,len(s)-1):
    
    # add to the string length if the alphabetical order is equal or greater
    if s[i] <= s[i+1] and len(longestString) < len(marker):
        marker += s[i+1]
        longestString = marker
        
    elif s[i] <= s[i+1]:
        marker += s[i+1]
        
    else:
        marker = s[i+1]

print('Longest substring in alphabetical order is: ' + longestString)
  