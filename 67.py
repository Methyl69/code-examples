studentdata = [[121, "able ","alice", 0.98],
               [124, "cooper", "charley", 1.0]]
foundstudent = []
mytarget=""

def findbysurname (ptarget, plist):
    index = 0
    moreitems= True
    found = False
    student = []

    while ((not found) and (moreitems)):
        if (plist[index][1] != ptarget):
            index = index +1
            if (index == len(plist)):
                moreitems =False

            else:
                    found  = True
                    student = plist[index]

                    return(student)

mytarget = "cooper"
print("target = " + mytarget)
foundstudent = findbysurname (mytarget, studentdata)
if (foundstudent ==[]):
    print (mytarget =  +"not found")
else:
    print (foundstudent)


mytarget = "murray"
print("n\target = " + mytarget)
foundstudent = findbysurname (mytarget, studentdata)
if (foundstudent ==[]):
    print (mytarget =  +"not found")
else:
    print (foundstudent)
