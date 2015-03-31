#!/usr/bin/env python
def counteng(string):
    words = len(string.split())
    string = string.upper()
    yuans = fus = 0
    for i in string:
        n = ord(i)
        if n in xrange(65,91):
            if n in [65,69,73,79,85]:
                yuans +=1
            else:
                fus +=1
    return (words,yuans,fus)


if __name__ == "__main__":
    string = raw_input("Please input a senctence: ")
    words = counteng(string)[0]
    yuanyin = counteng(string)[1]
    fuyin = counteng(string)[2]
    print "The sentence has %d words ,%d yuanyin , %d fuyin" %( words,yuanyin,fuyin)

