# s = 'azcbobobegghakl'
# s = 'abc'
#s = 'abcbcd'
s = 'axdjemzyljfjowtppdxhizji'

marker = s[0]
longestString = marker

for i in range(0,len(s)-1):
    
    # add to the string length if the alphabetical order is equal or greater
    if s[i] <= s[i+1]:
        marker += s[i+1]
    # start over with the marker check
    else:
        marker = s[i+1]
        
    if len(marker) > len(longestString):
        longestString = marker

print('Longest substring in alphabetical order is: ' + longestString)
  