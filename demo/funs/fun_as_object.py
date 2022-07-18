def fun():
    print("In fun()")


print(id(fun))
fun2 = fun
print(id(fun2))

fun()
fun2()

a = 10
print(id(a))
b = a
print(id(b))
