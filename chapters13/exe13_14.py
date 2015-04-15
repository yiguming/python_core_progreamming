#!/usr/bin/env python
import os 
def cmdDir():
    for i in os.listdir(os.getcwd()):
        print i+ " ",

def cmdMore(cmd):
    filename = cmd.split(" ")[1]
    with open (filename) as obj:
        for line in obj:
            print line,


def cmdType(cmd):   
    filename = cmd.split(" ")[1]
    return type(filename)

def cmdCopy(cmd):
    filename1 = cmd.split(" ")[1]
    filename2 = cmd.split(" ")[2]
    with open (filename1,"r") as fobj1:
        with open(filename2,"w") as fobj2:
            for line in fobj1:
                fobj2.write(line)

def cmdRem(cmd):
    cmdCopy(cmd)
    delFile = cmd.split(" ")[1]
    os.remove(delFile)

def cmdDel(cmd):
    delFile = cmd.split(" ")[1]
    os.remove(delFile)

def Dos():
    while True:
        cmd = raw_input("Pleae input the cmd:")
        if cmd.find("ls") != -1:
            cmdDir()
            print "\n"
        elif cmd.find("more") != -1:
            cmdMore(cmd)
        elif cmd.find("cat") != -1:
            print cmdType(cmd)
        elif cmd.find("cp") != -1:
            cmdCopy(cmd)
        elif cmd.find("mv") != -1:
            cmdRem(cmd)
        elif cmd.find("rm") != -1:
            cmdDel(cmd)
        else:
            print "input error"


if __name__ == "__main__":
    Dos()
