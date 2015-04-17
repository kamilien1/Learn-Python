def genPrimes():
    
    # for prime n+1, n+1%primes[2 to n] != 0
    
    primes = []
    count = 2
    
    while True:
        if len(primes) == 0:
            primes.append(2)
            yield primes[0]
            
        count+=1
        flag = True
            
        for i in primes:
            if count % i == 0:
                flag = False
       
        if flag == True:
            primes.append(count)
            yield count

      

a = genPrimes()
print a.next()
                   