num =int(input("enter an integer greater than 1:"))
isprime = 1
for i in range(2,num//2):
    if (num%i ==0):
        isprime = 0
    break
if(isprime == 1):
    print(num, "is prime")
else:
        print(num, "is not a prime number")
