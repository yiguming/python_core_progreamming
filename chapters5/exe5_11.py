#!/usr/bin/python
#print the even number from 0 to 20
def printevennumber(number1,number2):
    for x in range(number1,number2+1):
        if x % 2 == 0:
            print x,

def printoddnumber(number1,number2):
    for x in range(number1,number2+1):
        if x % 2 !=0:
            print x,


def ifdivide(number1,number2):
    if number1 % number2 == 0:
        return True
    else:
        return False





if __name__ == '__main__':
    printevennumber(0,20)
    print "\n"
    printoddnumber(0,20)
    print "\n"
    number1 = int(raw_input("Please input the first number: "))
    number2 = int(raw_input("Please input the second number: "))

    if ifdivide(number1,number2):
        print "%d can be divided by %d."%(number1,number2)
    else:
        print "%d can not be divided by %d."%(number1,number2)


