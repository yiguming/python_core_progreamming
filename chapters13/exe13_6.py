#!/usr/bin/env python
import math
class Point(object):
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def get_xy(self):
        return self.x,self.y
    def set_xy(self,point):
        self.x,self.y = point
    def __str__(self):
        return '%d,%d' %(self.x,self.y)
    __repr__ = __str__
    point = property(get_xy,set_xy)

class Line(object):
    def __init__(self,pointStart,pointEnd):
        self.pointStart= pointStart
        self.pointEnd = pointEnd
    def get_line(self):
        return self.pointStart,self.pointEnd
    def set_line(self,line):
        self.pointStart,self.pointEnd = line
    def __str__():
        return "%s-->%s" %(self.pointStart,self.pointEnd)
    def length(self):
        result= math.sqrt((self.pointStart.x - self.pointEnd.x) ** 2 + (self.pointStart.y - self.pointEnd.y) ** 2)
        return "%.2f" % result
    def slope(self,xielv=60):  
        self.xielv = xielv
    __repr__ = __str__
    line = property(get_line,set_line)

if __name__ == "__main__":
    p1 = Point(2,3)
    p2 = Point(6,9)
    line1 = Line(p1,p2)
    print line1.length()
