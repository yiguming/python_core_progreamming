#!/usr/bin/python
def teststrinclude(teststring,allstring):
    if teststring in allstring:
        result = True
    else:
        result = False
    return result


print teststrinclude("a","abc")
print teststrinclude("aaa","bbbaa")
