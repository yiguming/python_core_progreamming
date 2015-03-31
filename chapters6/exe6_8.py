#!/usr/bin/env python
def num2eng():
    new = []
    lists = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(lists)):
        print lists[i]
    iput = int(raw_input("Please input a number,range is in 0 ~1000: "))
    if iput <0 or iput > 1000:
        print "Error , not in the range!"
    else:
        iput = str(iput)
        for j in iput:
            new.append(lists[int(j)])
    return '-'.join(new)
       



if __name__ == "__main__":
    print num2eng()



