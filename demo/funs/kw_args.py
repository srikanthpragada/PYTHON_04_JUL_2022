def show(**kwargs):
    print(type(kwargs))
    print(kwargs)


def showall(*args, **kwargs):
    pass


show(a=10, b=20, n="Abc")
show(x=100, s="Pqr")

showall(10, 20, n="abc")
showall(10, 20, 20, n="abc", x=10)
