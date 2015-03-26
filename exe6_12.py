#!/usr/bin/env python
def findchr(string,char):
    index = 0
    if char in string:
        while (index < len(string)):
            if char == string[index]:
                return index
            else:
                index = index+1
    else:
        return -1




def rfindchr(string,char):
    index = 0
    if char in string:
        max_index = len(string) -1
        while (max_index>=0):
            if char == string[max_index]:
                return max_index
            else:
                max_index = max_index -1
    else:
        return -1



def subchr(string,origchar,newchar):
    index = 0
    newstr =[]
    if origchar in string:
        while (index < len(string)):
            if origchar == string[index]:
                newstr.append(newchar)
                index = index+1
            else:
                newstr.append(string[index])
                index = index +1
        return "".join(newstr)        
    else:
        return -1






if __name__ == "__main__":
    print findchr("abc","d")
    print rfindchr("zabcabcz","z")
    print subchr("abcabczbbbbbbbbbb","b","f")
