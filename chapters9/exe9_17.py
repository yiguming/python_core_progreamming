#!/usr/bin/env python
class FileEdit(object):
    def newfile(self,fileName,fileText):
        with open(fileName,"a+") as fobj1:
            fobj1.write(fileText)
    def showfile(self,fileName):
        strTemp = ""
        with open(fileName) as fobj1:
            for i in fobj1:
                strTemp +=i
        return strTemp
    def editfile(self,fileName,lineNum,newText):
        lines = []
        with open(fileName) as fobj1:
            lines = fobj1.readlines()
            if lineNum > len(lines):
                return False
            lines[lineNum-1] =newText + '\n'
        with open(fileName,"w") as fobj1:
            fobj1.writelines(lines)

if __name__ == "__main__":
    while True:
        fobj = FileEdit()
        print "n to newfile"
        print "s to showfile"
        print "e to editfile"
        print "q to exit"
        choice = raw_input("Please input the choice: ")
        if choice.lower() == "q":
            break
        if choice.lower() not in ['n','s','e','q']:
            continue
        else:
            if choice.lower() == "n":
                fileName = raw_input("Please input the name of the file: ")
                fileText = ""
                while True:
                    Text = raw_input("Please input the text(q to quit): ")
                    if Text.lower() == "q":
                        break
                    else:
                        fileText +=Text
                        fileText += "\n"
                fobj.newfile(fileName,fileText)
            elif choice.lower() == "s":
                fileName = raw_input("Please input the file: ")
                print fobj.showfile(fileName)
            elif choice.lower() == "e":
                fileName = raw_input("Please input the name of the file: ")
                lineNumber = int(raw_input("Please input the line number what you want to edit: "))
                lineText = raw_input("Please input the new text of you want to edit: ")
                fobj.editfile(fileName,lineNumber,lineText)
            




