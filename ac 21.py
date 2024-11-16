count = 1
number = 1

number = int(input ("Enter a number 1 for 12: "))

if (number < 1 ):
    print("number is small")
elif (number > 12):
    print ("num is too large")
    else:
        while(count <=12):
            print (str(number) + " x " + str(count) +
                   "=" + str(count * number))
            count = count + 1
