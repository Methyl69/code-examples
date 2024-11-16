base = 0.0
code = ""
realcost = 0.0


def calcost (pcode, pprice):
    realcost = 0.0

    if(pcode == "C"):
        realcost = pprice * (1- child)
    elif (pcode=="S"):
            realcost = pprice * (1 - senior)
        else : realcosr = pprice
        return (realcost)

base = float (input("enter the price in decimal:"))
code = input ("enter the C for child S for senior, any key for no code:")
code = code.upper ()
finalcost = calccost (code, base)
print ("your final cost is :" + str (final cost))

print ("goodbye")
        
