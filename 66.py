weeklystats =[23, 15, 6, 5, 2, 0, 0, 19, 15, 7, 3, 0, 3, 3,]

def findminimum (plist):
    minimum = 9999999

    for item in plist:
        if (item < minimum):
            minimum = item
            return (minimum)

def findmaximum(plist):
    maximum =0
    for item in plist:
        if (item >maximum):
            maximum = item
            return (maximum)

def findaverage (plist):
    total = 0
    avergae = 0.0
    for item in plist:
        total = total +item
        average = total/len(plist)
        return (average)
    
print(" min",findminimum(weeklystats))

print("max ",findmaximum(weeklystats))
print(" avg",findaverage(weeklystats))
