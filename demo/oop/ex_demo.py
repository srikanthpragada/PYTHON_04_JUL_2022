try:
    num = int(input("Enter number : "))
    result = 100 / num
    print(result)
except ValueError as ex:
    print('Please enter a valid number')
except ZeroDivisionError:
    print("Sorry! Zero is not valid!")

print("The End")

l = [1, 2, 3]
l.add(10)
