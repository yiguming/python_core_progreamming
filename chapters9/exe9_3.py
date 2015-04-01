#!/usr/bin/env python
def showline(filename):
    fobj = open(filename)
    line = 0
    for eachLine in fobj.readlines():
        line +=1
    fobj.close()
    return line

if __name__ =="__main__":
    filename = raw_input("Please input the name of the file: ")
    print showline(filename)
