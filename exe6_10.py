#!/usr/bin/env python

def l2uandu2l():
    istr = raw_input("Please input a string: ")
    newstr= []
    for char in istr:
        if char.isupper():
            newstr.append(char.lower())
        elif char.islower():
            newstr.append(char.upper())
        else:
            newstr.append(char)
    return "".join(newstr)


if __name__ == "__main__":
    
    print "After is : "+ l2uandu2l()
