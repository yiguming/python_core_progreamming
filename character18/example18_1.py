#!/usr/bin/env python
from time import sleep,ctime

def loop0():
    print 'loop0 start at:',ctime()
    sleep(4)
    print 'loop0 stop at:',ctime()

def loop1():
    print 'loop1 start at:',ctime()
    sleep(2)
    print 'loop1 stop at:',ctime()

def main():
    print 'starting at',ctime()
    loop0()
    loop1()
    print 'all DONE at',ctime()

if __name__ == "__main__":
    main()
