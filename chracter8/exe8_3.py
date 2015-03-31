#!/usr/bin/env python
def touchlist(a,b,c=1):
    alist = []
    for i in range(a,b,c):
        alist.append(i)
    return alist

if __name__ =="__main__":
    print touchlist(0,10)
    print touchlist(3,19,3)
    print touchlist(-20,861,220)
