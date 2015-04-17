
def fib(x, numCalls):
  
    numCalls += 1
    if x == 0 or x == 1:
        return 1, numCalls
    else:
        fibNum, numCalls = fib(x-1,numCalls)
        return fib(x-1,numCalls) + fib(x-2,numCalls)
    
    
