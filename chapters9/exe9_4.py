#!/usr/bin/env python
def readfile(filename,n):
    with open(filename,"a+") as fobj:
        for i in range(100):
            fobj.write(str(i))
            fobj.write("\n")
    with open(filename) as fobj:
        num =1
        for eachline in fobj:
            if num % (n+1) != 0:
                print eachline,
                num +=1
            else:
                go = raw_input("continue(c to continue ,other to quit): ")
                num +=1
                if go != "c":
                    break


if __name__ == "__main__":
    testname = raw_input("Please input the name of the file: ")
    showline = int(raw_input("Please input the number of the file: "))
    readfile(testname,showline)

