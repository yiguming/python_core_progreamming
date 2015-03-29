#!/usr/bin/env python
dic = {'c':1,'b':2,'a':3}
dic2 = {'a':3,'b':2,'c':1}
print dic
#exe 7_3_a
print "exe 7_3_a"
print sorted(dic)
print "exe 7_3_b"
#exe 7_3_b
for key in sorted(dic):
    print key,dic[key]
#exe 7_3_c
print "exe 7_3_c"
for value in sorted(dic2.values()):
    for key in dic2.keys():
        if dic2[key] == value:
            print key ,value



