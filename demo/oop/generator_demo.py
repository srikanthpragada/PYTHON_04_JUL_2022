def squares():   # Generator
    for n in range(1, 6):
        yield n * n


g = squares()
print(type(g))
print(next(g))
print(next(g))

for s in squares():
    print(s)

sqrs = (n * n for n in range(1, 6))  # Generator Expression
print(sqrs)

