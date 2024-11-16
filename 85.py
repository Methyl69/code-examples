num1 =0
num2 = 0

num1 = int (input("enter a number : "))
num2 = int (input("enter a second number: "))
if (num1 >= 1):
    if (num1 <= 10):
        if (num2 >= 11) and (num2<+ 20):
             print("valid")
        else:
         print("second number is invalid")
    else:
      print("first number too high")
else:
    print("first number too low")
