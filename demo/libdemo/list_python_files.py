import os

g = os.walk(r"c:\classroom\jul4\demo")

count = 0
for dname, dirs, files in g:
    for f in files:
        if f.endswith(".py"):
            print(dname + "\\" + f)
            count += 1


print("Count = ", count)
