# Display days in the given month

month = int(input('Enter month number :'))
if month == 2:
    print("28 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("30 days")
else:
    print("31 days")
