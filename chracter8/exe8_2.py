#!/usr/bin/env python
def coutprint(f,t,i):
    for num in range(f,t+1,i):
        print num,



if __name__ == "__main__":
    ifrom = int(raw_input("Please input the begin number: "))
    ito = int(raw_input("Please input the end number: "))
    iin = int(raw_input("Please input the increment: "))
    coutprint(ifrom,ito,iin)
