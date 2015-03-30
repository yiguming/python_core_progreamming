#!/usr/bin/env python
data = {}
listline = []
listotal = []

def datasys():
    while True:
        print "\ninput(id,shares,bprice,nprice)"
        while True:
            line = raw_input(">>").split()
            if len(line) <4:
                break
            linelist = list(line)
            listotal.append(linelist)
        lens = len(listotal)
        if lens<1:
            break
        inp = int(raw_input("Chose key (0,1,2,3)"))
        data=dict((listotal[i][inp],listotal[i][0:inp]+listotal[i][inp:])for i in range(lens))

        for key in sorted(data.keys()):
            print "%-6s%-6s%-6s%-6s"%(key,data[key][0],data[key][1],data[key][2])  
         
if __name__ == "__main__":
    datasys()

