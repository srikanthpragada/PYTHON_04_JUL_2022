# Display days in the given month

month = int(input('Enter month number :'))
if month == 2:
    year = int(input("Enter year :"))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("29 days")
    else:
        print("28 Days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
else:
    print("31 days")
