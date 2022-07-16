# Type annotations or hints

def line(length: int, ch: str):
    for i in range(length):
        print(ch, end='')

    print()


title = "Srikanth Technologies"
line(len(title), '*')
print(title)
line(len(title), '-')
