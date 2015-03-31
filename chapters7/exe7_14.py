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




orinput =  raw_input ("Please input A | B ")



print set(list(int_orinput))

#andinput = raw_input ("Please input A & B")
if set(list(orinput)) == (A|B):
    print "You are right or!"
else:
    print "Error!"


#if set(andinput) == (A & B):
#    print "You are right and!"
#else:
#    print "Error!"



print "The right answer is :"

print A | B
print A & B
