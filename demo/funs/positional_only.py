def line(length, ch, /):  # Positional-only
    for i in range(length):
        print(ch, end='')

    print()


line(10, '*')
# line(ch='-', length=10)
