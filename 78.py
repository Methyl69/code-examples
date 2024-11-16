import random
userroll = 0
computerroll = 0

userroll= int( input ("enter the roll of the dice:"))
if (userroll >= 1 ) and (userroll <=6 ):
    computerroll = random.randint (1,6)
    if (computerroll < userroll):
         print("you win :" + str(userroll) + "to computer " + str (computerroll))
    elif (computerroll >userroll):
         print("you lose :" + str(userroll) + "to computer " + str(computerroll))
    else:
             print("tie :" + str(userroll) + "to computer " + str(computerroll))
else:
    print("you win :" + str(userroll) + "to computer " + str(computerroll))
