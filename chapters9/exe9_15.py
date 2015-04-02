#!/usr/bin/env python
file1 = raw_input("Please enter file1: ")
file2 = raw_input("Please enter file2: ")
with open(file1) as fobj1:
    with open(file2,"w") as fobj2:
        for i in fobj1:
            fobj2.write(i)
    with open(file2) as fobj2:
        for i in fobj2:
            print i,
        
