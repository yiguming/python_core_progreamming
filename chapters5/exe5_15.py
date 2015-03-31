#!/usr/bin/env python
#-*- coding:utf-8 -*-
def zuidagongyueshu(number1,number2):
    temp = 0
    if (number1 < number2):
        number1,number2 = number2,number1
    while (number2 != 0):
        temp = number1 % number2
        number1 = number2
        number2 = temp
    return number1

def zuixiaogongbeishu(number1,number2):
    return number1 * number2 / zuidagongyueshu(number1,number2)






if __name__ == '__main__':
    print "最大公约数"
    print zuidagongyueshu(10,20)
    print zuidagongyueshu(20,10)
    print zuidagongyueshu(100,10)
    print zuidagongyueshu(30,70)

    
    print "\n"
    print "最小公倍数"
    print zuixiaogongbeishu(10,20)
    print zuixiaogongbeishu(20,10)
    print zuixiaogongbeishu(100,10)
    print zuixiaogongbeishu(30,70)

