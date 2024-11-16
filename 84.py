id = ""
num = 0
name = ""

num = int(input("enter a number: "))
name = input("enter a name:")

if (num>0) and (num <=99):
    if (len(name) > 0):
        id = name+ str(num)
        print(id)
    else:
        print ("invalid name")
else:
    print("invalid number")
