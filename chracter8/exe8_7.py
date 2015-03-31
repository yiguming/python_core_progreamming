#!/usr/bin/env python
def isperfect(number,addself= False):
    factorlist = []
    total = 0
    count = number / 2
    if addself: factorlist =[number]
    while count:
        if not number % count:
            factorlist.append(count)
        count -=1
    for num in factorlist:
        total +=num
    if total == number:
        return True
    else:
        return False




if __name__ == "__main__":
    print isperfect(6)
    for i in range(10000):
        if isperfect(i):
            print i,
