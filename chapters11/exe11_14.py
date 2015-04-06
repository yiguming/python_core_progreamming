#!/usr/bin/env python
def fibonacci(num):
    if num<1 or int(num)!=num:return False
    if num == 1:return 1
    re = 0
    for i in xrange(num-1):
        if re ==0 :N1,N2 = 0,1
        re = N1 + N2
        N1,N2 =N2,re
    return re


def fib(num):  
    a,b = 1,1  
    while num - 1:  
        a,b = b,a + b  
        num -= 1  
    return a

def new_fib(num, a = 1, b = 1):
    if num - 1:
        a,b = b,a+b
        return new_fib(num - 1, a, b)
    else:
        return a




if __name__ == "__main__":
    print fibonacci(6)
    print new_fib(8)
