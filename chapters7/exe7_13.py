import random

def rangeSet():
    ss = set()
    for i in range(10):
        ss.add(random.randrange(1,10))
    return ss
A = set()
A = rangeSet()
B = set()
B = rangeSet()
print A
print B
print A | B
print A & B
