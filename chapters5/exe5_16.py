#!/usr/bin/env python
def Payment(balance,payment):
    print "         Amount Remaining\n"
    print "Pymt#    Paid            Balance\n"
    print "----     -----           -------\n"
    print "0    $   % .2f    `   $ %.2f"%(0.00,balance )   
    i = 1
    while ((balance- payment*i) >0 ):
        print "%d    $  % .2f        $  %.2f"%(i,payment,balance-payment*i)
        i = i +1      
        if (balance - payment*i) <0:
            print "%d    $   % .2f        $  % .2f"%(i,balance-payment*(i-1),0.00)






if __name__ == '__main__':
    balance = float(raw_input("Enter opening balance: "))
    payment = float(raw_input("Enter monthly payment: "))
    Payment(balance,payment)
