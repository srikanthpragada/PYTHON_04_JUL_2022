for n in sorted([10, -3, 9, -13, 37, 45], key=abs):
    print(n)

print('-------------')

for n in sorted([10, -3, 9, -13, 37, 45]):
    print(n)


def second_value(t):
    return t[1]


for t in sorted([(1, 2), (5, 3), (4, 1), (2, 6)], key=second_value):
    print(t)
