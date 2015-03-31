#!/usr/bin/env python
def transmin2hour(miniutes):
    mins_part  = miniutes % 60
    hour_part = miniutes / 60
    return hour_part,mins_part


if __name__ == "__main__":
    imin = int(raw_input("Please input the minutes : "))
    print "hour is : " + str(transmin2hour(imin)[0])
    print "minutes is : " + str(transmin2hour(imin)[1])
