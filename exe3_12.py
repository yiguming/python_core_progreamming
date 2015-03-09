#!/usr/bin/python
#-*- coding:utf-8 -*-
#readNwriteTextFiles.py
import os
ls = os.linesep
class TextFile(object):
    """The class :TextFile"""
    selection1 = "(1)创建一个文本文件"
    selection2 = "(2)显示一个文本文件"
    
    def __init__(self):
    	"""init the five_number_list"""
	

    def showselection(self):
        print self.selection1
        print self.selection2

    def maketextfile(self):
        while True:
            self.filename = raw_input("Please input the file name:")
            if os.path.exists(self.filename):
                print "Error , '%s' is already exists" % self.filename
            else:
                break
        textlist = []
        print "input . is to stop the input"
        while True:
            entry = raw_input(">")
            if entry == ".":
                break
            else:
                textlist.append(entry)
        fobj = open(self.filename,'w')
        fobj.writelines('%s%s' %(x,ls) for x in textlist)
        fobj.close()

#readTextFile.py -- to read a file
    def readtextfile(self):
        try:
            self.filename = raw_input("Please input the file name:")
            fobj = open(self.filename,'r')
        except IOError,e:
            print "This file can not be open" ,e
        else:
            for eachLine in fobj.readlines():
	        print eachLine,
            fobj.close()
    
    def choice(self):
        choice = raw_input("Please input your choice: ")
        if choice =="1":
            self.maketextfile()
        elif choice == "2":
            self.readtextfile()
        else:
            print "input error"
            self.choice


if __name__ == "__main__":
    test = TextFile()
    test.showselection()
    test.choice()



