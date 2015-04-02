#!/usr/bin/env python
import os
from os import chdir,listdir
path = r'/usr/lib/python2.7'
chdir(path)
ls = [item for item in listdir(path) if item.endswith("py")]
db = {}.fromkeys(ls)
#print db

for item in ls:
    with open(item) as f:
        doc = ''
        start =  False
        for line in f:
            if line.strip().startswith('"""') and not start:
                start = True
                doc +=line
                if line.strip().endswith('"""') and len(doc.strip()) >3:
                    start = False
                    break
            elif line.strip().endswith('"""'):
                start = False
                doc += line
                break
            elif start:
                doc +=line
        db[item] = doc

empty = []
full = []
for key in sorted(db):
    if db[key] == '':
        empty.append(key)
    else:
        full.append(key)

print "moudles without doc"
for item in empty:
    print item
print 

print "moudles with doc"
for item in empty:
    print item
print 
print "value"
for key in full:
    print 'module:',key
    print 'doc:',db[key]








