names = ['java', 'javasript', 'c#', 'python', 'sql']

chars = set()   # empty set
for n in names:
    chars = chars | set(n)

print(chars)


