# Take a number and display factors

num = int(input("Enter number :"))

count = 0
for i in range(2, num // 2 + 1):
    if num % i == 0:
        count += 1


if count == 0:
    print("Prime Number")
else:
    print(f"Factors count = {count}")