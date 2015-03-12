#/usr/bin/python
meifen1 =1
meifen2 =5
meifen3 =10
meifen4 =25
def huanyingbi(money):
    number4 = money / 25
    number3 = (money - number4 * 25) / 10
    number2 = (money - number4 * 25 - number3 * 10)/5
    number1 = (money - number4 * 25 - number3 * 10 - number2 * 5)/1
    print ('The number of meifen1 is %d' % number1)
    print ('The number of meifen2 is %d' % number2)
    print ('The number of meifen3 is %d' % number3)
    print ('The number of meifen4 is %d' % number4)


money =int( float(raw_input("Please input a money value: ")) * 100)
#print money
huanyingbi(money)
