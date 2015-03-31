#!/usr/bin/python
#exe2_14
a = int(raw_input("Please input the first number: "))
b = int(raw_input("Please input the second number: "))
c = int(raw_input("Please input the third number: "))




if b > a:
    a,b = b,a
if c > a:
    a,c = c,a
if c > b :
    b,c = c,b
print "from the big to small."
print a,b,c




a = int(raw_input("Please input the first number: "))
b = int(raw_input("Please input the second number: "))
c = int(raw_input("Please input the third number: "))
if b < a:
   a,b = b,a
if c < a:
   a,c = c,a
if c < b :
   b,c = c,b





print "from the small to big"
print a,b,c
 
