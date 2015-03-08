#!/usr/bin/python
def number_test(number):
    if number > 0:
        print "The number %d is a zhengshu!" % number 
    elif number < 0:
	print "The number %d is a fushu!" % number
    else:
	print "The number %d is zero!" % number



number_test(1)
number_test(-1)
number_test(0)


for i in range(3):
    user_input =int( raw_input("Please input a number : "))
    number_test(user_input)



