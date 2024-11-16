weekly = [23, 15, 6, 5, 2, 0, 0, 19, 15 ,7 ,3, 0, 3, 3,]


def genstats (pList):
    min= 9999
    max= 0
    total = 0
    average= 0.0


for item in pList:
    total = total + item
    if (item < min):
       min = item
    if (item > max):
        max = item

    a = total / len (pList)

    print ("min", min , "max", max, "a", average )
genstats (weekly)
    
