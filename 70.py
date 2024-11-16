import random

MAX_POSSIBLE_VEG_NUMBER = 20
vegname = ""
vegnum =0
vegnumrandom = 0
vegname = input("enter the name of your favourite vegetable: ")
vegnum = int(input("how many" + vegname +"do you think you could eat?"))

print("so you think you can eat" + str (vegnum) + "" +vegname + " do you?")

vegnumrandom = random.randint (1, MAX_POSSIBLE_VEG_NUMBER)
print("the computer can eat" + str (vegnumrandom) + "" + vegname + ".")
