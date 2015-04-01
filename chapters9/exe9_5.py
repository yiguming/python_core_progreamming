def average_of_alist(alist):
    total  =0 
    for i in range(len(alist)):
        total += alist[i]
        average = float(total) / len(alist)
    return average


def printave(filename):
    numberlist = []
    with open(filename) as fobj :
        for eachLine in fobj:
            numberlist.append(int(eachLine))
    return numberlist


if __name__== "__main__":
    filename = raw_input("Please input the name of the file: ")
    scorelist = printave(filename)
    print average_of_alist(scorelist)    
