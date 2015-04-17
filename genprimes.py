import math

def genPrimes():
    count = 0
    one = 1
    while one == 1:
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                continue
            if count % x != 0:
                yield count

    	count += 1
    	
primeGenerator = genPrimes()
print primeGenerator.next()
primeGenerator.next()