sc =0
co =0
t= 0

co = int(input("enter a number of time sto loop (1-5)"))
sc = co
while (co >0):
    print ("loop count: "+ str(co))
    co = co-1
    sc = co + sc
    
 
print ("sum = " , sc)
