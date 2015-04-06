#!/usr/bin/env python
#-------------------a--------
def max2(num1,num2):
   return num1 if num1 > num2 else num2

def min2(num1,num2):
   return num1 if num1 < num2 else num2

print max2(4,8)
print min2(4, 8)

#-------------b--------------

def my_max(*args):
    return reduce(max2,args)



def my_min(*args):
    return reduce(min2,args)


print my_max(1,2,3,4,5,6,7,8)
print my_min(1,2,3,4,5,6,7,8)


 
