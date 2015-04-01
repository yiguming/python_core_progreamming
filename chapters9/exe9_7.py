#!/usr/bin/env python
def delmodule(name):
    obj = __import__(name)
    ls = dir(obj)
    for item in ls:
        print 'name: ', item
        print 'type: ', type(getattr(obj,item))
        print 'value ', getattr(obj,item)
        print 


if __name__ =="__main__":
    name = raw_input("Please input the module name:")
    delmodule(name)

