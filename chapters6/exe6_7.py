#!/usr/bin/env python
# input a nuber by user
num_str = raw_input('Enter a number: ')
#transfor the string type to the int type
num_num = int(num_str)

#print the range list
fac_list = range(1,num_num+1)
print "BEFORE:", fac_list

# set the index to 0
i = 0

# while loop
while i < len(fac_list):
    
    if num_num % fac_list[i] == 0 :
        del fac_list[i]
    i = i +1 


print "After: ",fac_list 
