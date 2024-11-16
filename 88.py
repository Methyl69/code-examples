nouns = ["cakes", "bicycle", "trees", "pigeons", "houses"]
verbs = ["eat", "ride", "hug" "case"]
sentence =""
userinput ="N"
while (userinput =="N"):
    nounindex = int (input("enter a noun index : "))
    verbindex = int (input ("enter a verb index: "))

    sentence + "the children"+ verbs [verbindex] + "" + nouns [nounindex] + "."
    print (sentence)

    userinput = input ("does this sentence make sense (Y/N)")
    userinput = userinput.upper()

print("goodbye")
