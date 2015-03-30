#!/usr/bin/env python
import string

numlower = ""
numupper = ""
numlower = string.lowercase * 2
numupper = string.uppercase * 2



def code_rot13(strTemp):
    newstring = ""
    for i in strTemp:
        if i.islower():
            newstring += numlower[numlower.find(i) + 13]
        elif i.isspace():
            newstring += i
        elif i == ".":
            newstring += i
        else:
            newstring += numupper[numupper.find(i) + 13]
    return newstring

if __name__ == "__main__":
    while True:
        string = raw_input("Enter string to rot13(-1 to quit):")
        if string == "-1":
            break
        #print "the code rot13 is:", code_rot13(string)
        print "Your string to en/decrypt was: " + "[", code_rot13(code_rot13(string)) + "]."
        print "The rot13 string is : " + "[", code_rot13(string) + "]."
