# Take names from user and write them into names.txt

f = open("names.txt", "at")   # append and text
while True:
    name = input("Enter name [end to stop] :")
    if name == "end":
        break

    f.write(name + "\n")

f.close()
