#!/usr/bin/env python
def fileread(fobj):
    for i in fobj:
        if i.startswith('#'):
            pass
        elif '#' in i:
            pass
        else:
            print i,


def fileopen(fobj):
    for i in fobj:
        print i,

if __name__ =="__main__":
    fobj = open('test.txt')
    print "Before filter"
    fileopen(fobj)
    fobj.close()
    fobj = open('test.txt')
    print "After filter"
    fileread(fobj)
    fobj.close()
