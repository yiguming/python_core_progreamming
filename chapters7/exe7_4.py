#!/usr/bin/env python
#exe7_4 
def hebinglist(alist,blist):
    '''hebing to list to be a dictory'''
    mydict = {}
    for i in range(len(alist)):
        mydict[alist[i]] = blist[i]
    return mydict

if __name__ == "__main__":
    alist = [1,2,3]
    blist =['abc','def','ghi']
    print hebinglist(alist,blist)
