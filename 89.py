theyear = 0
leapyear = False

theyear = int (input("enter a year(4 digits):"))
if (theyear < 1110):
    print("invalid input")
elif (theyear > 9999):
    print ("invalid input")
else:
    if (theyear %100 == 0):
        if (theyear % 400 ==0):
            leapyear = True
        else:
            lepayear = False
    elif (theyear %4 ==0):
        leapyear = True 
    else:
            leapyear = False
    if (leapyear):
     print (theyear, "is leap")
    else:
        print(theyear, "is not leap")
    
