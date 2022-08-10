def print_str(str, space=0):
    if len(str) != 0:
        print(' ' * space + str)
        print_str(str[1:], space + 1)


print_str('Shrink')
