bill = float()
tip =float()
tipvalue =float()
billtotal =float()

bill =0.0
tip =0.0
tipvalue =0.0
billtotal =0.0

bill =float(input("enter the bill amount: "))
tip =float (input("enter the % of the bill you want to leave as a tip: "))
tipvalue =bill * tip/100
billtotal =bill + tipvalue

print("the total cost is :", billtotal)
print("this includes a tip of ", tip, "percent, wich is", tipvalue)
