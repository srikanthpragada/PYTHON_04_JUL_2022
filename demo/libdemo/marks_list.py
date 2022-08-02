f = open("students.txt", "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue

    # print(parts)
    name = parts[0]
    marks = [int(m) for m in parts[1:] if m.isdigit()]
    total = sum(marks)
    print(f"{name:15} {total:3}  {total/len(marks):.2f} ")

f.close()
