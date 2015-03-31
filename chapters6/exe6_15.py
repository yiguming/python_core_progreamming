#!/usr/bin/env python
#-*- coding:utf-8 -*-
def datediff(date1,date2):    
    "利用datetime模块计算两个日期字串之间的天数，格式YYYY-MM-DD"
    if date1==date2:
        return 0
    from datetime import date
    d1=map(int,date1.split('-'))
    d2=map(int,date2.split('-'))
    d1=date(d1[0],d1[1],d1[2])
    d2=date(d2[0],d2[1],d2[2])
    return abs((d1-d2).days)
def dttoday(date1):
    "计算date1到今天的天数,date1格式为YYYY-MM-DD"
    from datetime import date
    date2= date.today().isoformat()
    return datediff(date1,date2) #利用上面的datedif(date1,date2)函数
def dtb(date1):
    "计算生日为date1的人还有多久过生日,date1格式为YYYY-MM-DD"
    from datetime import date
    today=date.today()
    d1=map(int,date1.split('-'))
    d1=date(today.year,d1[1],d1[2]) #今年的生日
    if today>d1: #如果今年已经过了生日，就计算到明年生日的天数
        d1=d1.replace(year=d1.year+1)
    return (d1-today).days



if __name__ == "__main__":
    print "The a question"
    date1 = raw_input("input the datetime YYYY-MM-DD:")
    date2 = raw_input("input another datetiem YYYY-MM-DD:")
    print datediff(date1,date2)

    print "The b question"
    date_birthday = raw_input("input the your bithday YYYY-MM-DD: ")
    print dttoday(date_birthday)

    print "The c question"
    date_birthday = raw_input("input the your bithday YYYY-MM-DD: ")
    print dtb(date_birthday)
