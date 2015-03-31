#!/usr/bin/env python
input_times = int(raw_input("Enter total number of names: "))
times = 0
names =[]
while times < input_times:
    wrongtimes =0
    name = raw_input("Please enter name %d: "%times)
    if len(name.split(',')) ==2:
        names.append(name.split(',')[0])
        names.append(name.split(',')[1])
    else:
        wrongtimes +=1
        print "Wrong format...should be Last, First."
        print "You have done this %d time(s) already ,Fixing input" % wrongtimes
    times +=1

print "The sorted list (by last name) is"
index = 0
while index < len(names):
    print "\t"+names[index]+' , '+names[index+1]
    index +=2



