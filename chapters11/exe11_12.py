#!/usr/bin/env python
import time
def testit(func,*nkwargs,**kwargs):
    try:
        retval = func(*nkwargs,**kwargs)
        result = (True,retval)
    except Exception,diag:
        result = (False,str(diag))
    return result


def test():
    funcs = (int,long,float)
    vals = (1234,12.34,'1234','12.34')

    for eachFunc in funcs:
        print '_'*20
        for eachVale in vals:
            retval = testit(eachFunc,eachVale)
            if retval[0]:
                print '%s(%s)= ' %(eachFunc.__name__,'eachVal'),retval[1]
            else:
                print '%s(%s)=FAILED:' %(eachFunc.__name__,'eachVal'),retval[1]

def timeit(fun,*argv):
    time1 = time.clock()
    time3 = time.time()
    for i in range(10000000):
        fun(*argv)
    time2 = time.clock()
    time4 = time.time()
    return time2 - time1,time4 - time3

def fun(*argv):
    return reduce(lambda x,y: x+y ,argv)




if __name__ == "__main__":
    print timeit(fun,1,2,3,4,5,6,7,8,9,10)
    
