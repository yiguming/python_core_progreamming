#!/usr/bin/env python
class StackQueue(object):
    def __init__(self,alist):
        self.alist = alist
    def isEmpty(self):
        return (not len(self.alist))
    def shift(self):
        if self.isEmpty():
            print "empyt ,can not shift"
        else:
            firstelement = self.alist[0]
            self.alist = self.alist[1:]
            return firstelement
    def unshift(self,element):
        self.alist = [element] + self.alist
    def push(self,element):
        self.alist.append(element)
    def pop(self):
        lastelement = self.alist[-1]
        self.alist = self.alist[:-1]
        return lastelement
    def __str__(self):
        return str(self.alist)
    __repr = __str__


if __name__ == "__main__":
    stkque = StackQueue([1,2,3])
    print stkque
    print stkque.shift()
    stkque.unshift(6)
    print stkque
    stkque.push(7)
    print stkque
    print stkque.pop()
    print stkque
    print stkque.__str__()
