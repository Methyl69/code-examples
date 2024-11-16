birds = ["robin", "birb", "blackbird", "joe" "sparrw"]
count = [1028, 1274, 1003, 1167, 1392]
index = 0

for index in range (0, len (birds)):
    print (birds[index] + "has a count of " + str(count[index]))

print ("--------")
index = 0
for item in birds:
    print(item + "has a count of " + str (count [index]))
    index = index + 1

print ("--------")
index = 0
while (index <len(birds)):
    print(birds[index] + "has a count of " + str(count [index]))
    print (birds [index] +" has a count of" + str(count[index]))
    index = index +1
