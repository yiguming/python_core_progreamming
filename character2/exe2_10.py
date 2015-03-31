#!/usr/bin/python
def number_test():
    while (1):
	number_test = int(raw_input("Please input a number: "))
	if number_test >= 1 and number_test <= 100:
	    print "Success! The number %d is in range of 1 to 100!" % number_test
	    break
	else:
	    print "Error input ,Please input again!"



number_test()





