#!/usr/bin/env python
#ip to int
def ip2int():
    ip = raw_input("Ip input: ")
    ips = ip.split(".")
    ip = []
    for i in xrange(0,4):
        ip.append(int(ips[i]))
        ip[i] = hex(ip[i])[2:]
        if len(ip[i]) ==1:
            ip[i] ='0' +ip[i]
    return int(ip[0]+ip[1]+ip[2]+ip[3],16)    


if __name__ == "__main__":
    print ip2int()
