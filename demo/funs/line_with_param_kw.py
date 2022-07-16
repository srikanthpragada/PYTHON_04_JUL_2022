def line(length, ch):
    for i in range(length):
        print(ch, end='')

    print()


line(20, '*')  # positional args
line(ch='-', length=30)  # keyword args
