#!/usr/bin/env python
def test(x):
    print "statement A"
    if x > 0:
        print "statement B"
        pass
    elif x < 0:
        print "statement C"
        pass
    else:
        print "statement D"
        pass
    print "statement E"

if __name__ == "__main__":
    print "a time x < 0"
    print "I guess A C E"
    print "Actual Result"
    test(-1)
    print "b time x ==0"
    print "I guess A D E"
    print "Actual Result"
    test(0)
    print "c time x >0"
    print "I guess A B E"
    print "Actual Result"
    test(1)

