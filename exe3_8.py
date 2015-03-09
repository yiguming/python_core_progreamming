#!/usr/bin/env python
#makeTextFile.py -- to make a file 
import os
#linesep is a enter char and using it can ignore the platform question 
ls = os.linesep

while True:
    filename = raw_input("Please input a filename for the file you created: ")
    if os.path.exists(filename):
	print "Error, '%s' is  already exists" % filename
    else:
	break
textlist = []

print "input . is to stop the input"
while True:
    entry  = raw_input("Current line inputing:")
    if entry == '.':
	break
    else:
	textlist.append(entry)
    
fobj = open(filename,'w')
fobj.writelines('%s%s' %(x,ls) for x in textlist)
fobj.close()






