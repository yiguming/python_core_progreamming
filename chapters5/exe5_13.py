#!/usr/bin/env python
def transfor(hour_time):
    timelist=hour_time.split(':')
    hour_part = timelist[0]
    min_part = timelist[1]
    total_min = int(hour_part) *60 + int(min_part)
    return total_min


if __name__ == '__main__':
    hour_time = raw_input("Please input the hour with min such like 3:50: ")
    print "%s is %d minites."%(hour_time,transfor(hour_time))
    

