#!/usr/bin/env python
name = raw_input("Please input the module name: ")
obj = __import__(name)
ls = dir(name)
for item in ls:
    print 'name:',item
    print 'type:',type(getattr(obj,item))
    print 'value',getattr(obj,item)
    print 
