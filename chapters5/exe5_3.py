#!/usr/bin/env python
while True:
    score = raw_input("Please input your testing score ")
    i_score = int(score)
    if (i_score >= 90) and (i_score <=100):
        print "You got A"
    elif (i_score >=80) and (i_score <=89):
        print "You got B"
    elif (i_score >=70) and (i_score <=79):
        print "You got C"
    elif (i_score >=60) and (i_score <=69):
        print "You got D"
    elif (i_score >=0) and (i_score <60):
        print "You got F"
    elif score == ".":
        break
    else:
        print "Input Error,Input again"

    
