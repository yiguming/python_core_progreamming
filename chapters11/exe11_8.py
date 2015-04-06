#!/usr/bin/python
def is_leap_year(year):
    if (year % 400 == 0) or ((year % 100 !=0) and (year % 4 ==0)):
        return True
    else:
        return False

def print_result(year):
    if is_leap_year(year):
        print "%d is a leap year" % year
    else:
        print "%d is not a leap year" % year



if __name__ == "__main__":
    yearlist = [1988,1882,1993,1992,1996,2000,1967,1990,2400]
    leapyearlist =  filter(is_leap_year,yearlist)
    print leapyearlist


    print "list jiexi method"
    print [year for year in yearlist if is_leap_year(year)]
