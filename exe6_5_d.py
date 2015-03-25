#!/usr/bin/env python
def backstring():
    istr = raw_input("Please input a string: ")
    return istr + istr[-1:-len(istr)-1:-1]

if __name__ =="__main__":
    print backstring()
