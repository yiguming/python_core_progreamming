#!/usr/bin/python
import os 
ls = os.linesep
        
while True:
    filename = raw_input("Please input a file name: ")
    try:
        if os.path.exists(filename):
            print "The file has exists!"
        else:
            break
    except IOError,e:
        print "Open File Error",e
    

textlist = []
print "input the . is to stop the input!"
while True:
    entry = raw_input("Please input something in the file: ")
    if entry == ".":
        break
    else:
        textlist.append(entry)


fobj = open(filename,'w')
fobj.writelines('%s%s'%(x,ls) for x in textlist)
fobj.close()








