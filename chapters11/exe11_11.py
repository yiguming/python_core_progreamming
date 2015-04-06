#!/usr/bin/env python 
import os
def newfile(filename1,filename2):
    with open(filename1) as fobj1:
        with open(filename2,"w") as  fobj2:
            for eachline in fobj1:
                fobj2.writelines(eachline.strip())
                fobj2.write('\n')

def overwrite(filename1):
    with open(filename1) as fobj1:
        with open('tempfile','w') as fobj2:
            for eachline in fobj1:
                fobj2.writelines(eachline.strip())
                fobj2.write('\n')
    os.remove(filename1)
    os.rename('tempfile',filename1)

if __name__ == "__main__":
    choice = raw_input("do you want to (N)ew a file or (O)verwirte the older file: ")
    if choice == "n":
        filename1 = raw_input("Please input the filename: ")
        filename2 = raw_input("Please input the new file name: ")
        newfile(filename1,filename2)
    elif choice =="o":
        filename1 = raw_input("Please input the filename: ")
        overwrite(filename1)
    else:
        print "Sorry,error input"




