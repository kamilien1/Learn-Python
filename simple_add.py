s = '1.2,3.4,3.24'
a = s.split(",")
sumTotal = 0
for i in range(0,len(a)):
    sumTotal+=float(a[i])
    
print sumTotal