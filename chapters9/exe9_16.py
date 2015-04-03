#/usr/bin/env python
import os
file1 = raw_input("please enter the file:")
with open(file1) as fobj1:
    with open("temp.txt","w") as fobj2:
        for i in fobj1:
            if len(i) > 80:
                num = list(i)
                count = len(num) / 80
                for i in range(count):
                    fobj2.write("".join(num[:79]))
                    fobj2.write("\n")
                    num = num[79:]
                fobj2.write("".join(num))
            else:
                fobj2.write(i)
                fobj2.write("\n")
with open("temp.txt") as fobj2:
    with open(file1,"w") as fobj1:
        for i in fobj2:
            fobj1.write(i)
os.remove("temp.txt")
