def line(length, ch):
    for i in range(length):
        print(ch, end='')

    print()
    

title = "Srikanth Technologies"
line(len(title), '*')
print(title)
line(len(title), '-')
