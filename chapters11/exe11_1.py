#!/usr/bin/env python
def countToFour1():
    try:
        for eachNum in range(5):
            print eachNum,
    except (NameError,TypeError),e:
        print e
def countToFour2(n):
    try:
        for eachNum in range(n,5):
            print eachNum,
    except (NameError,TypeError),e:
        print e

def countToFour3(n=1):
    try:
        for eachNum in range(n,5):
            print eachNum,
    except (NameError,TypeError),e:
        print e

count = 0
while count < 3:
    num = int(raw_input("Please input a number: "))
    countToFour1()
    print "\n"
    countToFour2(num)
    print "\n"
    countToFour3(num)
    print "\n"
    count +=1


