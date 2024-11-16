mylist = [150, 153, 163, 198, 200, 210, 212, 217, 215,
          263, 281, 311, 318, 365, 376, 401, 411, 441,
          583, 616, 620, 636, 716, 802, 807, 807, 840,
          841, 877, 896]
def forwardtraversal(inlist):
    index = 0

    for number in inlist:

         if(index==0):
            print(inlist[index])
         if(index == len (inlist) - 1):
            print (inlist[index])
         index =index+1

forwardtraversal(mylist)
