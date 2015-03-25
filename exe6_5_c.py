#!/usr/bin/python
import string
# control char include 0~31 and 127 and whitespace
def isback():
    denny  = [chr(i) for i in xrange(0,32)] + list(string.whitespace)
    denny.append(chr(127))

    strs = raw_input("Please input the string: ")
    news = []
    for i in strs:
        if i in denny:continue
        news.append(i)



    lens= len(news)
    if (lens % 2) != 0:
        result = False
    else:
        half = lens/2
        if news[0:half] == news[-1:-half-1:-1]:
            result =  True
        else:
            result = False

    return result

if __name__ == "__main__":
   print  isback()
