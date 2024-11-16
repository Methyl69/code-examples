total = 0.0
number = 0
size= ""
cs= 10.25
cm = 12.88
cl = 15.25

number = float(input("enter number of shirts:"))
size = str(input("enter yo size (S,M,L):"))

if ( size == "S"):
  size = cs
elif ( size== "M"):
  size = cm
else:
 size = cl

total = number * size
print ("your total is", total )


            
