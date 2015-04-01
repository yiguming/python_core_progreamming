#!/usr/bin/env python
#  -*- coding: utf-8 -*-
def readfile(filename,num):
    open_filename = open(filename)
    for eachline in open_filename:
        if num:
            print eachline,
            num -= 1
        else:
            break
    open_filename.close()


if __name__ == "__main__":
    filename = raw_input('Please enter the filename of F:')
    num = int(raw_input('Please enter the num of N:'))
    readfile(filename,num)
