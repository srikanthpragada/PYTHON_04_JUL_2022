def line(*, length, ch):  # Keyword-only
    for i in range(length):
        print(ch, end='')

    print()


# line(10, '*')
line(ch='-', length=10)
