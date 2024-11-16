mylist = [150, 153, 163, 198, 200, 210, 212, 217, 215,
          263, 281, 311, 318, 365, 376, 401, 411, 441,
          583, 616, 620, 636, 716, 802, 807, 807, 840,]
def reversesearch (inlist, intarget):
    index =0
    found =False
    passed =False

    index =len (inlist) - 1
    while ((index >= 0) and (not found) and (not passed)):
        if (inlist[index] == intarget):
            found = True
        else:
            index = index -1

    if (found):
        print( intarget, "found at index", index)
    else:
        print (intarget, "notfound")

reversesearch (mylist,636)
reversesearch (mylist,150)
reversesearch (mylist, 130)
reversesearch (mylist,896)
reversesearch (mylist,720)
reversesearch (mylist,900)
