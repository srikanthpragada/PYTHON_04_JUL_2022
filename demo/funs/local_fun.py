g = 1000  # Global variable


def fun1():
    global g
    a = 10
    print('fun1')
    g = 2000

    def fun2():  # Local function
        nonlocal a
        b = 100  # Local variable
        a = 20
        print('fun2')
        print(g, a, b)  # Enclosing variable

    fun2()
    print(a)


fun1()
