#!/usr/bin/env python
def isprime(num):
    count = num /2
    while count >1:
        if num % count == 0 :
            return False
        count -=1
    return True

def primefactors(number):
    re =[]
    if isprime(number): re =[1,number] 
    else:
        prime = 2
        count = number / 2
        while prime < count+1:
            if number % prime == 0:
                number /= prime
                re.append(prime)
                continue
            prime +=1
    return re    


if __name__ == "__main__":
    print primefactors(10)
    print primefactors(20)
    print primefactors(50)
    print primefactors(100)
