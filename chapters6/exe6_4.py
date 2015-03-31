#!/usr/bin/python
def average_of_alist(alist):
    total  =0 
    for i in range(len(alist)):
        total += alist[i]
        average = float(total) / len(alist)
    return average


score_list = []
n =0
Times = 10
while True:
    score =  raw_input("Please input your testing score ")
    i_score = int(score)
    if n == Times:
        break
    if (i_score >= 90) and ( i_score <=100):
        print "You got A"
        score_list.append(i_score)
        n = n +1
    elif (i_score >=80) and (i_score <=89):
        print "You got B"
        score_list.append(i_score)
        n = n +1
    elif (i_score >=70) and (i_score <=79):
        print "You got C"
        score_list.append(i_score)
        n = n +1
    elif (i_score >=60) and (i_score <=69):
        print "You got D"
        score_list.append(i_score)
        n = n +1
    elif (i_score >=0) and (i_score <60):
        print "You got F"
        score_list.append(i_score)
        n = n +1
    else:
        print "Input Error,Input again"


print average_of_alist(score_list)



