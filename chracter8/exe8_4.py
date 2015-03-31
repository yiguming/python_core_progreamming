#!/usr/bin/env python
def isprime(num):
    count = num /2
    while count >1:
        if num % count == 0 :
            return False
        count -=1
    return True




if __name__ == "__main__":
    print isprime(14)
    print isprime(7)
