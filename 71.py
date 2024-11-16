planettable = ["MERCURY", "VENUS", "EARH", "MARS", "JUPITER", "SATURN", "URANUS", "NEPTUNE"]
outstring = ""
found = False
index = 0

for planet in planettable:
    outstring = outstring + planet + ""
print(outstring)

target = input ("enter a planet to find: ")
target = target.upper ()

while((not found)) and (index < len(planettable)):
    if(target == planettable[index]):
        found = true
    else:
            index = index + 1

if (not found):
    print(target + "not found")
else:
    print(target + "form at index" + str (index))
    
