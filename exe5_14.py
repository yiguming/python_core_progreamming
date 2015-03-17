#!/usr/bin/env python
def huibao(basemoney,rate):
    totalmoney = basemoney*(1+rate)*365
    huibao = totalmoney / float(basemoney)
    print "The basemoney %.2f ,after a year it will be change %.2f ,and the huibaolv is %f"%(basemoney,totalmoney,huibao)
    

if __name__ == "__main__":
    huibao(100.00,0.25)

    
