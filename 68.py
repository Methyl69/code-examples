# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
studentData = [[121, "Able", "Alice", 0.98],
               [123, "Bennett", "Bob", 0.87],
               [124, "Cooper", "Charley", 1.0],
               [125, "Davies", "Danil", 0.97],
               [126, "Edgar", "Eliott", 0.99],
               [129, "Forest", "Frankie", 0.88],
               [130, "Granger", "George", 0.94]]
foundStudent = []               # Empty list
myNumber = 0
mySurname = ""

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def findBySurname (pTarget, pList):
    index = 0
    moreItems = True            # Assume you have items
    found = False               # Assume not found yet
    student = []                # The one we're looking for

    while ((not found) and (moreItems)):
        if (pList[index][1] != pTarget):    # Not this one, so go forward
            index = index + 1               # Check if all items seen
            if (index == len(pList)):       # No more, stop loop, return invalid
                moreItems = False
        else:                           # It is the target, stop loop
            found = True
            student = pList[index]

    return (student)

def findByNumber (pTarget, pList):
    index = 0
    moreItems = True            # Assume you have items
    found = False               # Assume not found yet
    student = []                # The one we're looking for

    while ((not found) and (moreItems)):
        if (pList[index][0] != pTarget):    # Not this one, so go forward
            index = index + 1               # Check if all items seen
            if (index == len(pList)):       # No more, stop loop, return invalid
                moreItems = False
        else:                           # It is the target, stop loop
            found = True
            student = pList[index]

    return (student)

def getStudentNumber ():
    stdNumInt = 0
    stdNumString = ""
    valid = False

    while (not valid):
        stdNumString = input ("Enter a student number: ")
        if (stdNumString != ""):       # Presence
            if (len (stdNumString) != 3):   # Length
                print ("Input must be four digits long")
            else:
                stdNumInt = int (stdNumString)
                valid = True
        else:
            print ("Input cannot be empty")

    return (stdNumInt)

def getStudentSurname():
    stdName = ""
    valid = False

    while (not valid):
        stdName = input("Enter a student surname: ")
        if (stdName != ""):  # Presence
            if (len (stdName) < 4 or (len (stdName) > 20)):  # Length
                print("Name must be between 4 and 20 characters")
            else:
                valid = True
        else:
            print("Input cannot be empty")

    return (stdName)

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------

myNumber = getStudentNumber()
print ("Target = " + str(myNumber))
foundStudent = findByNumber (myNumber, studentData)
if (foundStudent == []):
    print (str (myNumber) + " not found")
else:
    print (foundStudent)

mySurname = getStudentSurname()
print ("Target = " + mySurname)
foundStudent = findBySurname (mySurname, studentData)
if (foundStudent == []):
    print (mySurname + " not found")
else:
    print (foundStudent)
