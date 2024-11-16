total = 0.0
num =0
size= ""
sm = 10.25
cm= 12.88
cl = 15.25

num = int(input ("enter no of shirts "))
size = input("enter S,M or L")

size = size.upper()

if (size =="S"):
    total = num *cs
elif (size =="M"):
    total = num * cm
else:
    
    (size =="L"):
    total = num * cl

        

print (" total is"+ str(total))
