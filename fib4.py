def f(n, ncalls=0):
    ncalls += 1
    if n == 1:
        return 1, ncalls
    else:
        res, ncalls = f(n-1, ncalls)
        return n * res, ncalls

for n in xrange(1, 6):
    print 'f({}): {:4d} ({} calls)'.format(n, *f(n))