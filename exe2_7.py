#!/usr/bin/python
# print every char of a string from a user inputL
# while loop
user_input = raw_input("Please input a string:")
# using while loop
print "using while loop"
i =0
while (i < len(user_input)):
    print user_input[i],
    i+=1

#using while loop
print 
print "Using for loop"
for char in user_input:
    print char,


