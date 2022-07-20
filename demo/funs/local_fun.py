g = 1000  # Global variable


def fun1():
    a = 10
    print('fun1')

    def fun2():  # Local function
        b = 100  # Local variable
        print('fun2')
        print(g, a, b)  # Enclosing variable

    fun2()


fun1()
