#!/usr/bin/env python
import math
def isprime(n):
    if n <=1:
        return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n % i == 0 :
            return False
        return True



if __name__ == "__main__":
    print isprime(14)
    print isprime(7)
