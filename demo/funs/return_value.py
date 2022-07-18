def num_type(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


def count_upper(st):
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return count


def has_digit(st):
    for c in st:
        if c.isdigit():
            return True

    return False


t = num_type(10)
print(t)
print(count_upper("AbcXyz"))
print(has_digit("abc"), has_digit("X3931ABC"))
