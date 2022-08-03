f = open("employees.txt", "rt")

depts = {}
for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) != 2:
        continue

    dept, emp = parts
    employees = depts.get(dept, [])
    employees.append(emp)
    depts[dept] = employees

f.close()

for name, employees in sorted(depts.items()):
    print(f"{name:10} {','.join(sorted(employees))}")



