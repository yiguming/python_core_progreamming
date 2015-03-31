#!/usr/bin/python
#!/usr/bin/python
#readTextFile.py -- to read a file
filename = raw_input("Please input a filename: ")
try:
    fobj = open(filename,'r')
except IOError,e:
    print "This file can not be open" ,e
else:
    for eachLine in fobj.readlines():
        print eachLine.strip()
    fobj.close()


