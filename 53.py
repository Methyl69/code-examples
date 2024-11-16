sum = 0
number = int(input("enetr an integer:"))
while (number!= 0):
    digit = number%10
    sum = sum + digit

    number = number //10
print("sum of digit is: ", sum)
