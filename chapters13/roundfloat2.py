#!/usr/bin/env python
class RoundFloatManual(object):
    def __init__(self,val):
        assert isinstance(val,float),\
            "Value must be a float!"
        self.value = round(val,2)
    
    def __str__(self):
        return '%.2f' % self.value



if __name__ =="__main__":
    rfm = RoundFloatManual(5.590464)
    rfm2 = RoundFloatManual(5.5964)
    print rfm
    print rfm2
