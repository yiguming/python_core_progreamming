#!/usr/bin/env python
def comparefile(file1,file2):
    fobj1 =open(file1)
    fobj2 =open(file2)
    line1 = fobj1.readlines()
    line2 = fobj2.readlines()
    for i in range(min(len(line1),len(line2))):
        if line1[i] != line2[i]:
            print i+1
            break
    fobj1.close()
    fobj2.close()


if __name__ == "__main__":
    filename1 = raw_input("Please input the name of the first file: ")
    filename2 = raw_input("Please input the name of the second file: ")
    comparefile(filename1,filename2)



