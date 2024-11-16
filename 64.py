weeklystats =[23, 15, 6, 5, 2, 0, 0, 19, 15, 7, 3, 0, 3, 3,]
messages =["error", "ok", "ok","error","error", "ok","ok",]

def countofoccurences(plist, ptarget):
    count= 0
    for item in plist:
        if (item ==ptarget):
            count = count+1
            print(str(ptarget) + "occurs" + str(count) + "times")

countofoccurences(messages, "error")
countofoccurences(weeklystats, 0)
