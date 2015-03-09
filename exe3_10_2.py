#!/usr/bin/python
import os 
while True:
    filename =raw_input("Please input a filename for the file you created: ")
    if os.path.exists(filename):
        fobj = open(filename,'r')
        for eachLine in fobj.readlines():
            print eachLine,
        fobj.close()
        break
    else:
        print "can not find the file!"
        


