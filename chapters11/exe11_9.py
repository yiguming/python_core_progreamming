#!/usr/bin/env python
def average(alist):
    for num in  alist:
        total = reduce((lambda x,y: x + y),alist)
        lens = len(alist)
        average = float(total) /lens
    return average

if __name__ == "__main__":
    testlist = [1,2,3,4,5,6,7,8,9,10]
    print average(testlist)
