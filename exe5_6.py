#!/usr/bin/python
while 1:
    expression = raw_input ('Please input a express just like number1 +,-,*,/,%,** number2 :')
    if  '+' in expression:
        exlist = expression.split()
        result=  float(exlist[0]) +float(exlist[2])
        print result
    elif '-' in expression:
        exlist = expression.split()
        result = float(exlist[0]) - float(exlist[2])
        print result
    elif '*' in expression:
        exlist = expression.split()
        result = float(exlist[0]) * float(exlist[2])
        print result
    elif '/' in expression:
        exlist = expression.split()
        if float(exlist[2]) == 0:
            print "can not be divided by zero"
        else:
            result = float(exlist[0]) / float(exlist[2])
            print result
    elif '%' in expression:
        exlist = expression.split()
        result = float(exlist[0]) % float(exlist[2])
        print result
    elif '**' in expression:
        exlist = expression.split()
        result = float(exlist[0]) ** float(exlist[2])
        print result
    else:
        print "input error ,Please input again!"
    



    
