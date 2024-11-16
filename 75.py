import random
import math
import time

MAX_COUNT = 100
PI =math.pi
mylist = []
mean = 0.0
abovepi = 0

def genrandomreals (plist, pcount):
    number = 0.0
    for count in range (0, pcount):
        number =random.random () * 10
        plist.append (number)

def countabovepi (plist):
    count = 0
    for index in range (0, len(plist)):
        if(plist[index]> PI):
            count = count + 1
            return (count)

def findmean(plsit):
    mean = 0.0
    total = 0.0
    for index in range (0, len(plist)):
        total = total + plist[index]

mean =total/ len (plist)
return (mean)
print("generating numbers..?")
time.sleep (1)
getrandomreals (mylist, MAX_COUNT)
print(mylist)

print("calculating no above pi")
abovepi =countabovepi (mylist)
print ("above Pi :", above pi)

print ("calculating the mean")
print ("mean ", mean)
print("goodbye")

