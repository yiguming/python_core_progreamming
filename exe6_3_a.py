#!/usr/bin/python
numberlist= []
        
n =1
while 1:
    try:
        number_input = int(raw_input("Please input the number: ")) 
        numberlist.append(number_input)
        n = n+1
        if n == 10:
            break
    except ValueError,e:
        print "Error!",e



numberlist.sort()
print numberlist
