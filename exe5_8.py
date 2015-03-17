#!/usr/bin/python
import math
PI = math.pi
class Square(object):
    def __init__(self ,a=5):
        self.bianchang = a
    def mianji(self):
        return self.bianchang ** 2
    def tiji(self):
        return self.bianchang ** 3

class Ball(object):
     #   result = 0
    def __init__(self, r = 5):
        self.banjing = r
    def mianji(self):
        return   PI * (self.banjing ** 2)
    def tiji(self):
        return  (4/3.0) * PI * (self.banjing ** 3)
       # print "%.2f" % self.result

num = int( raw_input("Please input a number:"))


testsquare  = Square(num)
print "The mianji of Square bianchang %d is %.2f" % (num,testsquare.mianji())
print "The tiji of Square bianchang %d is %.2f" % (num,testsquare.tiji())


testball = Ball(num)
print "The mianji of Ball banjing %d is %.2f" % (num,testball.mianji())
print "The tiji of Ball banjing %d is %.2f" %(num,testball.tiji())




