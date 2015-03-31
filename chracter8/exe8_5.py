#!/usr/bin/env python
def getfactors(number):
    factorlist = []
    for i in range(1,number+1):
        if number % i == 0:
            factorlist.append(i)
    return factorlist

if __name__ == "__main__":
    while True:
        testnumber = int(raw_input("Please input a number: "))
        if str(testnumber) == ".":
            break
        else:
            print getfactors(testnumber)



