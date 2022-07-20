for n in sorted([10, -3, 9, -13, 37, 45], key=abs):
    print(n)

print('-------------')

for n in sorted([10, -3, 9, -13, 37, 45]):
    print(n)

for t in sorted([(1, 2), (5, 3), (4, 1), (2, 6)], key=lambda t: t[1]):
    print(t)

persons = {'Bill': 60, 'Scott': 34, "Tom": 24, 'Larry': 55}

for name, age in sorted(persons.items(), key=lambda t: t[1]):
    print(f"{name:10} {age:2}")
