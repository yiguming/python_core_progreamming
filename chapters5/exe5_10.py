def FtransforC(F):
    c = (F - 32) * (5.0/9)
    return c

Ft = float(raw_input("Please input the f tem:"))

if __name__ == '__main__':
    print "%.2f"% FtransforC(Ft)
