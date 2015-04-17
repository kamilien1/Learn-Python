s = 'azcbobobegghakl'

bobCount = 0

i = 0

while i < len(s):
        if 'bob' in s[i:i+3].lower():
            bobCount+=1 
        i+=1
        
print('Number of times bob occurs is: ' + str(bobCount))

