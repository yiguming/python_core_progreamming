#!/usr/bin/env python
# create a string.stip() to del the space in the top or the end in the string
def delstrip(astring):
    newstring = []
    for char in astring:
        if char != " ":
            newstring.append(char)
        else:
            pass
    anewstring = "".join(newstring)
    return anewstring

print delstrip("   abc   ") + "!"
print delstrip("aaa   ") +"!"
print delstrip("   bbb") + "!"
