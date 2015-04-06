#!/usr/bin/env python
import time
def mult(x,y):
    return x*y

def diedai(n):
    ji = 1
    for i in range(1,n+1):
        ji =ji *i
    return ji

def fac1(n):
    return reduce(mult,range(1,n+1))

def fac2(n):
    return reduce(lambda x,y:x * y ,range(1,n+1))

def factorial(n):
    if n == 0 or n ==1: 
        return 1
    else:
        return (n * factorial(n-1))

def timeit(fun,*argv):
    time1 = time.clock()
    time3 = time.time()
    for i in range(10000000):
        fun(*argv)
    time2 = time.clock()
    time4 = time.time()
    return time2 - time1,time4 - time3


if __name__ =="__main__":
    print "diedai method"
    print "test clocktime is %f,test timetime is %f" %( timeit(diedai,10)[0],timeit(diedai,10)[1])
    print "reduce method"
    print "test clocktime is %f,test timetime is %f" %( timeit(fac2,10)[0],timeit(fac2,10)[1])
    print "digui method"
    print "test clocktime is %f,test timetime is %f" %( timeit(factorial,10)[0],timeit(factorial,10)[1])
    #print timeit(factorial,10)
    

