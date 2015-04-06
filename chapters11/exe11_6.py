#!/usr/bin/env python
def printf(fmt,*arg):
    print fmt % arg
 
if __name__ == "__main__":
    printf('%d',10)
    printf('%f',10.1)
    printf('%s','abc')
