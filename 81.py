import math
usernumber = 0.0
userround = 0.0
userfloor = 0
userround =0
usernumber =float (input ("enter a number with 5 decimal plaes (0 to extit): "))
while (usernumber !=0):
    userfloor = math.floor(usernumber)
    userceiling = math.ceil(usernumber)
    userround = round(usernumber, 3)

    print (usernumber, userfloor, userceiling, userround)
    usernumber = float(input("enter a number with five decimal places(o to exit):"))

    print("goodby")
