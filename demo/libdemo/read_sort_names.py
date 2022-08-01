f = open("names.txt", "rt")

lines = filter(lambda l: len(l.strip()) > 0, f.readlines())

for line in sorted(lines):
    print(line.strip())

f.close()
