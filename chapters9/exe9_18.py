#!/usr/bin/env python
filechar = raw_input("Please input the charater you want to count: ")
filename = raw_input("Please input the name of the file: ")
countNum  = 0
with open(filename) as fobj:
    for i in fobj:
        countNum +=i.count(filechar)
print "character %s occurs %d times." % (filechar,countNum)



