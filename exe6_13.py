#!/usr/bin/env python
def atoc(string):
    cindex = string.rfind('-')
    if cindex <= 0:
        cindex = string.rfind("+")
    if cindex > 0:
        real = float(string[0:cindex])
        compl = float(string[cindex:-1])
    return complex(real,compl)


if __name__ == "__main__":
    print atoc('-1.23e+4-5.67j')
        
