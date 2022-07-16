# Default arguments
def line(length=30, ch='-'):
    for i in range(length):
        print(ch, end='')

    print()


line()
line(40)
line(20, '*')
line(ch='*')
