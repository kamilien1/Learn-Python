s = 'azcbobobegghakl'
countTotal = 0

for char in s:
    if char.lower() in 'aeiou':
        countTotal+=1

print(countTotal)
