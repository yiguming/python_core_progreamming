#!/usr/bin/env python
def rochambeau():
    import random
    select = ["paper","shears","rock"]
    cli = int(raw_input("input your select [1.paper 2.shears 3.rock]"))-1
    print "--- You VS Computer ---"
    print '\nYou [%s]' % select[cli],
    cup = random.choice([0,1,2])
    print '\nComputer [%s]\n' % select[cup]
    youwin = "---You Win!!!---"
    cupwin = "---Computer Win!!! ---"
    eq = "---Nobody win---"

    if cli == cup:
        print eq
        return 
    if cup - cli == -2 or (cup > cli and (cli- cup != -2)):
        print cupwin
    else:
        print youwin


if __name__ == "__main__":
    rochambeau()


