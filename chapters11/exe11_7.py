#!/usr/bin/env python
alist = [1,2,3]
blist = ['abc','def','ghi']

print "map function"
print map(None,alist,blist)


print "map lambda function"
print map(lambda x,y: (x,y) ,alist,blist )


print "zip function"
print zip(alist,blist)

