def fib(x):
    global numCalls
    numCalls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
    
def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print 'fib i=',i,' is',fib(i)
        print 'numCalls is',numCalls