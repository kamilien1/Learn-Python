def removeDups(d1,d2):
    for e1 in d1:
        if e1 in d2:
            d1.remove(e1)

d1 = [1,2,3,4]
d2 = [3,4,5,6,7]

removeDups(d1,d2)
print d1,'\n', d2