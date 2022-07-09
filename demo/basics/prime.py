# Take a number and display whether it is prime number

num = int(input("Enter number :"))
prime = True
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print("Not a prime number")
        prime = False
        break   # terminate loop

if prime:
    print("Prime Number")



