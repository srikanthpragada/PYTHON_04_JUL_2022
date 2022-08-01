f = open("students.txt", "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    # print(parts)
    name = parts[0]
    marks = map(int, parts[1:])   # Convert str to int
    print(f"{name:15} {sum(marks):3}")

f.close()
