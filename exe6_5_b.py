#!/usr/bin/python
def mycmp():
    str1 = raw_input("Please input the first string: ")
    str2 = raw_input("Please input the second string: ")
    cha = len(str1) - len(str2)
    if cha != 0:
        return False
    for i,j in enumerate(str1):
        if ord(j) - ord(str2[i]):
            return False
    return True



if __name__ == "__main__":
    print mycmp()
        
