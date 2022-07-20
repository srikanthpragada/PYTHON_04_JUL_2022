def inc(v):
    print(id(v))
    v = v + 1
    print(id(v), v)


a = 100    # Immutable object
print(id(a))
inc(a)
print(a)


def prepend(lst, value):
    lst.insert(0, value)


l = [1, 2, 3]   # Mutable object
prepend(l, 100)
print(l)
