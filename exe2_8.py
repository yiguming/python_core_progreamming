#!/usr/bin/python
#return the sum of a stable list or tuple using while or for
number_list = [1,2,3,4,5]
number_tuple = (2,3,4,5,6)

#using while loop 
def total_while(list_or_tuple):
    i = 0
    total = 0
    while (i < len(list_or_tuple)):
	total += list_or_tuple[i]
	i +=1
    return total 


#using for loop
def total_for(list_or_tuple):
    total =0
    for i in range(len(list_or_tuple)):
	total += list_or_tuple[i]
    return total


def total_while_user_input():
    i = 0 
    total = 0
    list_or_tuple = []
    input_times= 0
    while (input_times<5):
	number_input = int(raw_input("Please input the %dth number: " %(input_times +1)))
	list_or_tuple.append(number_input)
        input_times +=1
    while (i < len(list_or_tuple)):
	total += list_or_tuple[i]
	i +=1
    print "The input list is " ,list_or_tuple
    return total


def total_for_user_input():
    total = 0
    list_or_tuple = []
    for i in range(5):
	number_input = int(raw_input("Please input the %dth number:" % (i+1)))
	list_or_tuple.append(number_input)
    for i in range(len(list_or_tuple)):
	total += list_or_tuple[i]
    print "The input list is ", list_or_tuple
    return total



print "test list for while loop function"
print total_while(number_list)
print "test tuple for while loop function"
print total_while(number_tuple)

print "test list for for loop function"
print total_for(number_list)
print "test tuple for while loop function"
print total_for(number_tuple)

print "test list for while loop user input function"
print total_while_user_input()

print "test list for for loop user input function"
print total_for_user_input()


