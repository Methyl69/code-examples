animals = ["fish", "hedgehog", "cat", "rabbit", "guinea pig", "moose"]
choice = 0
found = False
index = 0
print(animals)
choice = int(input("enter anummber"))
while((not found) and (index < len(animals))):
    if (len(animals[index]) == choice):
        found = True
        print("the pet is" + animals[index])
    else:
        index = index + 1
if (not found):
    print("sorry no pet")
