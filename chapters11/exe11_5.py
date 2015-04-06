#!/usr/bin/python
def calshui(price,shui=0.03):
    print "The shui is %.2f" %(price * shui)



if __name__ == "__main__":
    price = float(raw_input("Please input the price :"))
    calshui(price)
    calshui(price,0.05)
