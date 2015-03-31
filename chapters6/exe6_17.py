#!/usr/bin/env python
def mypop(alist):
    del alist[len(alist)-1]
    return alist[len(alist)-1]
    

if __name__ == "__main__":
    testlist =[1,2,3]
    print mypop(testlist)
