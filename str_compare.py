str1 = raw_input("enter in string 1:\n")
str2 = raw_input("enter in string 2:\n")

if str1 in str2:
    print 'all good'
elif str2 in str1:
    print 'also all good'
else:
    print 'no string in common found'