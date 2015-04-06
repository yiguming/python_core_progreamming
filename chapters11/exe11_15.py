def printLeft(strTemp):
    if strTemp:
        print strTemp[0],
        return printLeft(strTemp[1:])
def printRight(strTemp):
    if strTemp:
        print strTemp[-1],
        return printRight(strTemp[:-1])

if __name__ =="__main__":
    printLeft("hello world!")
    print 
    printRight("hello world!")






