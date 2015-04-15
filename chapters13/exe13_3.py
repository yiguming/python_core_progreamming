#!/usr/bin/evn python
def dollarize(fValue):
        strValue = str(fValue)
        isNegative = False
        if strValue[0] == "-":
            isNegative = True
            strValue = strValue[1:]
        strMoney = strValue.split(".")
        strTemp = []
        while (len(strMoney[0]) - 1) / 3:
            strTemp.append(strMoney[0][-3:])
            strMoney[0] = strMoney[0][:-3]
        strTemp.append(strMoney[0])
        strTemp.reverse()
        myDoller = ",".join(strTemp) + "." + strMoney[1]
        if isNegative:
            myDoller = "-" + myDoller
        return myDoller


class MoneyFmt(object): 
    def __init__(self,value=0.0):
        self.value = dollarize(value)
    def update(self,value = None):
        self.value = dollarize(value)
    def __nonzero__(self):
        return bool(self.value)
    def __repr__(self):
        return repr(self.value)
    def __str__(self):
        val = '$'
        if self.value[0] == "-":
            val = "-$" + self.value[1:]
        else:
            val +=self.value
        return val





if __name__ == "__main__":
    floatnumber = 1234567.8901
    floatnegative = -1234567.8901
    print dollarize(1234567.8901)
    print dollarize(floatnegative)


    cash = MoneyFmt(1234567.8901)
    print cash
    nagecash = MoneyFmt(-1234567.8901)
    print nagecash
    cash.update(111111.11111)
    print cash
    print cash.__nonzero__()
    print cash.__repr__()
    print cash.__str__()
    nagecash.update(-1111111.111111)
    print nagecash
    print nagecash.__nonzero__()
    print nagecash.__repr__()
    print nagecash.__str__()

