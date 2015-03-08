#!/usr/bin/python
def average_of_alist(list_or_tuple):
    total  =0 
    for i in range(len(list_or_tuple)):
	total += list_or_tuple[i]
    average = float(total) / len(list_or_tuple)
    return average



testlist = [1,2,3,4,5]
testtuple = (1,2,3,4,5)


print "print the test list"
print testlist
print "print the average of a list"
print average_of_alist(testlist)

print "print the test tuple"
print testtuple
print "print the average of a tuple"
print average_of_alist(testtuple)


