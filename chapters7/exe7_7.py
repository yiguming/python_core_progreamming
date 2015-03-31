#/usr/bin/env python
#diandao dict key and value
def diandao(adict):
    reversedict = {}
    for key in adict:
        reversedict[adict[key]] = key
    return reversedict



if __name__ =="__main__":
    testdict = {'a':1,'b':2,'c':3}
    print "older dict is " ,testdict
    print "new dict is ",diandao(testdict)
