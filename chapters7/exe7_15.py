def heihei(set1, set2, op):
    return eval(str(set1) + str(op) + str(set2))
if __name__ == "__main__":
    while True:
        num1 = raw_input("please enter set1,like(1,2,3)(q to qiut):")
        if num1.lower() == "q":
            break
        num2 = raw_input("please enter set2,like(1,2,3)(q to quit):")
        if num2.lower() == "q":
            break
        op = raw_input("please enter the operator(q to quit):")
        if op.lower() == "q":
            break
        print "([%s]) %s ([%s]) is: %s" % (num1, op, num2, heihei(set(num1.split(","),set(num2.split(","),op))))
