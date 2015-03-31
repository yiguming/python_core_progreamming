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

print_result(1992)
print_result(1996)
print_result(2000)
print_result(1967)
print_result(1990)
print_result(2400)
