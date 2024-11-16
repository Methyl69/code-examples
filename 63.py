def genstats(plist):
    min = 9999
    max = 0
    total = 0
    average = 0.0

for item in plist:
    total =total + item
    if (item< min):
        min =item
        if (item >max):
            max = item

average = total /len(plist)
print("min:" ,min, "avg", average, "max", max)
